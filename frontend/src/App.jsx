import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import TeamList from './components/TeamList';
import TeamForm from './components/TeamForm';
import TeamDetail from './components/TeamDetail';

import './styles/styles.scss';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<TeamList />} />
                <Route path="/teams" element={<TeamList />} />
                <Route path="/teams/new" element={<TeamForm />} />
                <Route path="/teams/:id" element={<TeamDetail />} />
                <Route path="/teams/:id/edit" element={<TeamForm />} />
            </Routes>
        </Router>
    );
}

export default App;
