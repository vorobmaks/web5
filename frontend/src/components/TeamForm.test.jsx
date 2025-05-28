import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { MemoryRouter, Route, Routes } from 'react-router-dom';

import TeamForm from './TeamForm';

beforeEach(() => {
    global.fetch = jest.fn();
});

afterEach(() => {
    jest.resetAllMocks();
});

test('додає нову команду', async () => {
    global.fetch.mockResolvedValue({
        ok: true,
    });

    render(
        <MemoryRouter initialEntries={['/teams/new']}>
            <Routes>
                <Route path="/teams/:id" element={<TeamForm />} />
                <Route path="/teams/new" element={<TeamForm />} />
            </Routes>
        </MemoryRouter>,
    );

    fireEvent.change(screen.getByLabelText(/Team Name/i), {
        target: { name: 'team_name', value: 'Test FC' },
    });
    fireEvent.change(screen.getByLabelText(/City/i), {
        target: { name: 'city', value: 'Lviv' },
    });
    fireEvent.change(screen.getByLabelText(/Stadium/i), {
        target: { name: 'stadium', value: 'Arena Lviv' },
    });

    fireEvent.click(screen.getByRole('button', { name: /Add Team/i }));

    await waitFor(() => {
        expect(global.fetch).toHaveBeenCalledWith(
            '/api/teams/',
            expect.objectContaining({
                method: 'POST',
            }),
        );
    });
});

test('завантажує дані команди для редагування', async () => {
    global.fetch.mockResolvedValueOnce({
        ok: true,
        json: jest.fn().mockResolvedValue({
            team_name: 'Edited Team',
            city: 'Kyiv',
            stadium: 'NSC Olimpiyskiy',
        }),
    });

    render(
        <MemoryRouter initialEntries={['/teams/1']}>
            <Routes>
                <Route path="/teams/:id" element={<TeamForm />} />
            </Routes>
        </MemoryRouter>,
    );

    expect(await screen.findByDisplayValue('Edited Team')).toBeInTheDocument();
    expect(screen.getByDisplayValue('Kyiv')).toBeInTheDocument();
    expect(screen.getByDisplayValue('NSC Olimpiyskiy')).toBeInTheDocument();
});

test('видаляє команду при натисканні Delete', async () => {
    global.fetch
        .mockResolvedValueOnce({
            ok: true,
            json: jest.fn().mockResolvedValue({
                team_name: 'To Delete',
                city: 'City',
                stadium: 'Stadium',
            }),
        }) // GET
        .mockResolvedValueOnce({ ok: true }); // DELETE

    render(
        <MemoryRouter initialEntries={['/teams/1']}>
            <Routes>
                <Route path="/teams/:id" element={<TeamForm />} />
            </Routes>
        </MemoryRouter>,
    );

    const deleteButton = await screen.findByText(/Delete Team/i);
    fireEvent.click(deleteButton);

    await waitFor(() => {
        expect(global.fetch).toHaveBeenCalledWith('/api/teams/1/', {
            method: 'DELETE',
        });
    });
});
