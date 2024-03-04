import { writable } from 'svelte/store';

// Inicjalizacja stanu
const initialState = {
    loggedIn: false,
    userData: null,
    token: null, 
    sessionId: null,
    password: null,
};

// Tworzenie writable store
export const authStore = writable(initialState);

// Funkcje pomocnicze
export function setLoggedIn(isLoggedIn, username, token, sessionId, password) {
    authStore.update(store => {
        store.loggedIn = isLoggedIn;
        store.userData = username;
        store.token = token;
        store.sessionId = sessionId;
        store.pasword = password
        return store;
    });
}

export const logout = () => {
    authStore.update(state => {
        return { ...state, loggedIn: false, userData: null };
    });
};