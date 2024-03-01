import { writable } from 'svelte/store';

// Inicjalizacja stanu
const initialState = {
    loggedIn: false,
    userData: null
};

// Tworzenie writable store
export const authStore = writable(initialState);

// Funkcje pomocnicze
export const setLoggedIn = (loggedIn, userData = null) => {
    authStore.update(state => {
        return { ...state, loggedIn, userData };
    });
};

export const logout = () => {
    authStore.update(state => {
        return { ...state, loggedIn: false, userData: null };
    });
};