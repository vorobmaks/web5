import React from 'react';
import { render, screen } from '@testing-library/react';

import App from './App';

beforeEach(() => {
    global.fetch = jest.fn(() =>
        Promise.resolve({
            json: () => Promise.resolve([]),
        }),
    );
});

test('рендерить головну сторінку', async () => {
    render(<App />);

    expect(await screen.findByText(/Team Management/i)).toBeInTheDocument();
});
