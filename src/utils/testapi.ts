import { api } from "../main";

export async function testCreateArticle() {
  try {
    const response = await api.createArticle("tag", "name", "content");
    return { success: true, data: response, name: "CREATE Article" };
  } catch (error) {
    return { success: false, error: error, name: "CREATE Article" };
  }
}

export async function testUpdateArticle() {
  try {
    const response = await api.updateArticle("tag", "name", "new content");
    return { success: true, data: response, name: "UPDATE Article" };
  } catch (error) {
    return { success: false, error: error, name: "UPDATE Article" };
  }
}

export async function testUploadMedia() {
  try {
    const buffer = await api.uploadMedia('tag', 'name', 'videos', 'video.heif', new File([''], 'video.heif', { type: 'video/heif' }));
    return { success: true, data: buffer, name: "UPLOAD Media" };
  } catch (error) {
    return { success: false, error: error, name: "UPLOAD Media" };
  }
}

export async function testGetVideo() {
  try {
    await api.getMedia("tag", "name", "videos", "video.heif");
    return { success: true, name: "GET Media" };
  } catch (error) {
    console.log(error)
    return { success: false, error: error, name: "GET Media" };
  }
}

export async function testGetArticle() {
  try {
    const article = await api.getArticle("tag", "name");
    return { success: true, data: article, name: "GET Article" };
  } catch (error) {
    return { success: false, error: error, name: "GET Article" };
  }
}

export async function testGetArticleMetadata() {
  try {
    const metadata = await api.getArticleMetadata();
    return { success: true, data: metadata, name: "GET Article Metadata" };
  } catch (error) {
    return { success: false, error: error, name: "GET Article Metadata" };
  }
}

export async function testDeleteMedia() {
  try {
    await api.deleteMedia("tag", "name", "videos", "video.heif");
    return { success: true, name: "DELETE Media" };
  } catch (error) {
    return { success: false, error: error, name: "DELETE Media" };
  }
}

export async function testDeleteArticle() {
  try {
    await api.deleteArticle("tag", "name");
    return { success: true, name: "DELETE Article" };
  } catch (error) {
    return { success: false, error: error, name: "DELETE Article" };
  }
}
