const BASE_API = (import.meta.env.VITE_BASE_API ?? "http://127.0.0.1:8000");

export async function getHomeMessage() {
  const response = await fetch(`${BASE_API}/home/`);
  return response.text();
}

export const getHomepageAPI = getHomeMessage;

export const dailyTrackAPI = {
  list: async () => {
    const response = await fetch(`${BASE_API}/dailytrack/`);
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      const err = new Error(data.detail || data.error || 'Request failed');
      err.response = { data };
      throw err;
    }
    return data;
  },
  create: async (dailytrack) => {
    const response = await fetch(`${BASE_API}/dailytrack/create/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dailytrack),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      const err = new Error(data.detail || data.error || 'Request failed');
      err.response = { data };
      throw err;
    }
    return data;
  },
  update: async (id, dailytrack) => {
    const response = await fetch(`${BASE_API}/dailytrack/${id}/update/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dailytrack),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      const err = new Error(data.detail || data.error || "Request failed");
      err.response = { data };
      throw err;
    }
    return data;
  },
  delete: async (id) => {
    const response = await fetch(`${BASE_API}/dailytrack/${id}/delete/`, {
      method: "DELETE",
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      const err = new Error(data.detail || data.error || "Request failed");
      err.response = { data };
      throw err;
    }
    return data;
  },
}