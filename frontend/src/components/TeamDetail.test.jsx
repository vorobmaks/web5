import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import { MemoryRouter, Route, Routes } from 'react-router-dom';

import TeamDetail from './TeamDetail';

global.fetch = jest.fn(() =>
    Promise.resolve({
        json: () =>
            Promise.resolve({
                id: 1,
                team_name: 'Team A',
                city: 'Kyiv',
                stadium: 'Olimpiyskiy',
            }),
    }),
);

test('відображає деталі команди', async () => {
    render(
        <MemoryRouter initialEntries={['/teams/1']}>
            <Routes>
                <Route path="/teams/:id" element={<TeamDetail />} />
            </Routes>
        </MemoryRouter>,
    );

    await waitFor(() => {
        expect(screen.getAllByText('Team A')).toHaveLength(2);
        expect(screen.getByText(/Kyiv/)).toBeInTheDocument();
    });
});
