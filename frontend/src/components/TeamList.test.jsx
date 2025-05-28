import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';

import TeamList from './TeamList';

global.fetch = jest.fn(() =>
    Promise.resolve({
        json: () => Promise.resolve([{ id: 1, team_name: 'Team A' }]),
    }),
);
test('відображає список команд після завантаження', async () => {
    render(
        <MemoryRouter>
            <TeamList />
        </MemoryRouter>,
    );
    await waitFor(() => expect(screen.getByText('Team A')).toBeInTheDocument());
});
