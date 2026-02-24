import { Link } from "react-router-dom";
import { dailyTrackAPI } from "../../service/api";
import { useEffect, useState } from "react";
import UpdateDailyTrack from "./UpdateDailyTrack.jsx";
import DeleteDailyTrack from "./DeleteDailyTrack.jsx";

function ListDailyTrack() {
  const [list, setList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [editingItem, setEditingItem] = useState(null);
  const [deletingItem, setDeletingItem] = useState(null);

  useEffect(() => {
    fetchTrackList();
  }, []);

  const fetchTrackList = async () => {
    setLoading(true);
    setError("");
    try {
      const data = await dailyTrackAPI.list();
      setList(Array.isArray(data) ? data : []);
    } catch (err) {
      setError(
        err.response?.data?.detail || err.message || "Failed to load daily track"
      );
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="max-w-6xl mx-auto px-4 py-12 flex justify-center">
        <p className="text-slate-600 text-lg">Loading…</p>
      </div>
    );
  }
  if (error) {
    return (
      <div className="max-w-6xl mx-auto px-4 py-12">
        <p role="alert" className="text-red-600 bg-red-50 border border-red-200 rounded-lg px-4 py-3">
          Error: {error}
        </p>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <Link
        to="/dailytrack/create"
        className="mb-6 inline-flex items-center rounded-lg bg-slate-700 px-4 py-2.5 text-sm font-medium text-white shadow-sm transition-colors hover:bg-slate-600 focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-offset-2"
      >
        Add Daily Track
      </Link>
      <h1 className="text-2xl font-bold text-slate-800 mb-6">Daily Course</h1>
      <ul className="space-y-4">
        {list.map((item) => (
          <li
            key={item.id}
            className="bg-white border border-slate-200 rounded-lg p-4 shadow-sm hover:shadow-md transition-shadow"
          >
            <strong className="text-slate-800">{item.title}</strong>
            <span className="text-slate-500 ml-2">— {item.date}</span>
            {item.description && (
              <p className="mt-2 text-slate-600 text-sm">{item.description}</p>
            )}
            {item.updated_at && (
              <p className="mt-1.5 text-slate-400 text-xs">Updated at {item.updated_at}</p>
            )}
            <div className="mt-3 flex gap-2">
              <button
                type="button"
                onClick={() => setEditingItem(item)}
                className="rounded-md border border-slate-300 bg-white px-3 py-1.5 text-sm font-medium text-slate-700 shadow-sm transition-colors hover:bg-slate-50 focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-offset-2"
              >
                Edit
              </button>
              <button
                type="button"
                onClick={() => setDeletingItem(item)}
                className="rounded-md border border-red-200 bg-white px-3 py-1.5 text-sm font-medium text-red-600 shadow-sm transition-colors hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
              >
                Delete
              </button>
            </div>
          </li>
        ))}
      </ul>
      {list.length === 0 && (
        <p className="text-slate-500 text-center py-8">No daily tracks yet.</p>
      )}
      {editingItem && (
        <UpdateDailyTrack
          item={editingItem}
          onClose={() => setEditingItem(null)}
          onSuccess={() => fetchTrackList()}
        />
      )}
      {deletingItem && (
        <DeleteDailyTrack
          item={deletingItem}
          onClose={() => setDeletingItem(null)}
          onSuccess={() => fetchTrackList()}
        />
      )}
    </div>
  );
}

export default ListDailyTrack;