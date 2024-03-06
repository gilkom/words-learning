import { writable } from 'svelte/store';

// Inicjalizacja stanu
const initialState = {
    loggedIn: false,
    userData: null,
    id: null,
};

// Tworzenie writable store
export const authStore = writable(initialState);

// Funkcje pomocnicze
export function setLoggedIn(isLoggedIn, username, id) {
    authStore.update(store => {
        store.loggedIn = isLoggedIn;
        store.userData = username;
        store.id = id
        return store;
    });
}

export const logout = () => {
    authStore.update(state => {
        return { ...state, loggedIn: false, userData: null, id: null };
    });
};