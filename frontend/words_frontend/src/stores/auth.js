import { writable } from 'svelte/store';
import { browser } from '$app/environment';

// Inicjalizacja stanu
const initialState = {
    loggedIn: false,
    userData: null,
    id: null,
    regular: null,
};

let storedState = initialState;
if (browser) {
    const stored = localStorage.getItem('authState');
    if (stored) {
        storedState = JSON.parse(stored);
    }
}


// Tworzenie writable store
export const authStore = writable(storedState);

// Funkcje pomocnicze
export function setLoggedIn(isLoggedIn, username, id, regular) {
    authStore.update(store => {
        store.loggedIn = isLoggedIn;
        store.userData = username;
        store.id = id;
        store.regular = regular
        if (browser) {
            localStorage.setItem('authState', JSON.stringify(store));
        }
        return store;
    });
}

export const logout = () => {
    authStore.update(state => {
        return { ...state, loggedIn: false, userData: null, id: null, regular: true};
    });
    if (browser) {
        localStorage.removeItem('authState');
    }
};