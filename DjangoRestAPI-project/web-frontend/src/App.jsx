import React from "react";
import { Routes, Route } from "react-router-dom";
import "./App.css";
import NavBar from "./components/NavBar.jsx";
import Homepage from "./components/Homepage.jsx";
import ListDailyTrack from "./pages/daily_track/ListDailyTrack.jsx";
import CreateDailyTrack from "./pages/daily_track/CreateDailyTrack.jsx";

function App() {
  return (
    <>
      <NavBar />
      <main className="min-h-screen bg-slate-100">
        <Routes>
          <Route path="/home" element={<Homepage />} />
          <Route path="/dailytrack" element={<ListDailyTrack />} />
          <Route path="/dailytrack/create" element={<CreateDailyTrack />} />
        </Routes>
      </main>
    </>
  );
}

export default App;