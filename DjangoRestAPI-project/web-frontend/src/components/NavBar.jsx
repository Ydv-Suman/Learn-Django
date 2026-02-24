import React from "react";
import { Link } from "react-router-dom";

function NavBar() {
  return (
    <div className="bg-slate-800 text-white shadow-lg">
      <header className="max-w-6xl mx-auto px-4 py-4">
        <nav className="flex items-center gap-6">
          <Link to="/home" className="text-xl font-semibold hover:text-amber-400 transition-colors">
            Django + React
          </Link>
          <Link to="/dailytrack" className="text-slate-300 hover:text-white transition-colors">
            DailyTrack
          </Link>
          <span className="text-slate-500 cursor-default">About</span>
        </nav>
      </header>
    </div>
  );
}

export default NavBar;
