import {writable} from 'svelte/store'

const initialState = {
    word_id: null,
    word: null,
    translation: null,
    example_sentence: null,
    owner: null,
};


export const WordStore = writable([])

