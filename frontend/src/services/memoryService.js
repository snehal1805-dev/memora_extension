import axios from "axios";

// Railway Backend URL
const API_URL = "https://memoraextension-production.up.railway.app";

const getAuthConfig = () => {

    const token =
        localStorage.getItem("access_token") ||
        localStorage.getItem("token");

    return {
        headers: {
            Authorization: `Bearer ${token}`
        }
    };

};

// =========================
// SAVE MEMORY
// =========================

export const saveMemory = async (data) => {

    const response = await axios.post(
        `${API_URL}/memory/save`,
        data,
        getAuthConfig()
    );

    return response.data;

};

// =========================
// DASHBOARD STATS
// =========================

export const getDashboardStats = async () => {

    const response = await axios.get(
        `${API_URL}/memory/dashboard`,
        getAuthConfig()
    );

    return response.data;

};

// =========================
// RECENT MEMORIES
// =========================

export const getRecentMemories = async () => {

    const response = await axios.get(
        `${API_URL}/memory/recent`,
        getAuthConfig()
    );

    return response.data;

};

// =========================
// ALL MEMORIES
// =========================

export const getAllMemories = async (params = {}) => {

    const response = await axios.get(
        `${API_URL}/memory/all`,
        {
            ...getAuthConfig(),
            params
        }
    );

    return response.data;

};

// =========================
// FAVORITES
// =========================

export const getFavoriteMemories = async () => {

    const response = await axios.get(
        `${API_URL}/memory/favorites`,
        getAuthConfig()
    );

    return response.data;

};

// =========================
// TOGGLE FAVORITE
// =========================

export const favoriteMemory = async (id) => {

    const response = await axios.patch(
        `${API_URL}/memory/favorite/${id}`,
        {},
        getAuthConfig()
    );

    return response.data;

};

export const toggleFavorite = favoriteMemory;

// =========================
// UPDATE MEMORY
// =========================

export const updateMemory = async (id, data) => {

    const response = await axios.patch(
        `${API_URL}/memory/update/${id}`,
        data,
        getAuthConfig()
    );

    return response.data;

};

// =========================
// DELETE MEMORY
// =========================

export const deleteMemory = async (id) => {

    const response = await axios.delete(
        `${API_URL}/memory/delete/${id}`,
        getAuthConfig()
    );

    return response.data;

};

// =========================
// SEARCH MEMORIES
// =========================

export const searchMemories = async (query) => {

    const response = await axios.post(
        `${API_URL}/memory/search`,
        {
            query
        },
        getAuthConfig()
    );

    if (Array.isArray(response.data)) {
        return response.data;
    }

    return [];

};

// =========================
// TOP TAGS
// =========================

export const getTopTags = async () => {

    const response = await axios.get(
        `${API_URL}/memory/dashboard/top-tags`,
        getAuthConfig()
    );

    return response.data;

};

// =========================
// TOP DOMAINS
// =========================

export const getTopDomains = async () => {

    const response = await axios.get(
        `${API_URL}/memory/dashboard/top-domains`,
        getAuthConfig()
    );

    return response.data;

};

// =========================
// MOST VISITED
// =========================

export const getMostVisited = async () => {

    const response = await axios.get(
        `${API_URL}/memory/dashboard/most-visited`,
        getAuthConfig()
    );

    return response.data;

};

// =========================
// AI INSIGHT
// =========================

export const getAIInsight = async () => {

    const response = await axios.get(
        `${API_URL}/memory/dashboard/insight`,
        getAuthConfig()
    );

    return response.data;

};