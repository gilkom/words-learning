import { writable } from 'svelte/store';

// Inicjalizacja stanu
const initialState = {
    loggedIn: false,
    userData: null,
};

// Tworzenie writable store
export const authStore = writable(initialState);

// Funkcje pomocnicze
export function setLoggedIn(isLoggedIn, username) {
    authStore.update(store => {
        store.loggedIn = isLoggedIn;
        store.userData = username;
        return store;
    });
}

export const logout = () => {
    authStore.update(state => {
        return { ...state, loggedIn: false, userData: null };
    });
};