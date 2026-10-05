// Defaults follow the host the page was opened from, so the app also works
// when opened from another device on the network (e.g. http://192.168.1.20:5174),
// not only on localhost. Set the VITE_* variables to override.
const HOST = `${window.location.protocol}//${window.location.hostname}`;

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || `${HOST}:5000/api/v1`;
export const LANDING_URL = import.meta.env.VITE_LANDING_URL || `${HOST}:5172`;
export const SELLER_PORTAL_URL = import.meta.env.VITE_SELLER_PORTAL_URL || `${HOST}:5173`;
export const BUYER_PORTAL_URL = import.meta.env.VITE_BUYER_PORTAL_URL || `${HOST}:5174`;
