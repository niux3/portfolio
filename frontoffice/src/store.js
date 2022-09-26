import { writable } from 'svelte/store';

export const current_view = writable(window.location.hash.length === 0? "#/accueil" : window.location.hash);