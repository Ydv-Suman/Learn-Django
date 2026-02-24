import React, { useState, useEffect } from "react";
import { getHomepageAPI } from "../service/api";

function Homepage() {
  const [detail, setDetail] = useState("");

  useEffect(() => {
    getHomepageAPI()
      .then(setDetail)
      .catch(() => setDetail("Could not load message"));
  }, []);

  return (
    <div className="max-w-6xl mx-auto px-4 py-12 text-center">
      <h1 className="text-3xl font-bold text-slate-800">{detail}</h1>
    </div>
  );
}

export default Homepage;