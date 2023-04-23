import { api } from "../main";

export async function testCreateArticle() {
  try {
    const response = await api.createArticle("workflow", "test_article");
    return { success: true, data: response, name: "CREATE Article" };
  } catch (error) {
    return { success: false, error: error, name: "CREATE Article" };
  }
}

export async function testUpdateArticle() {
  try {
    const response = await api.updateArticle("workflow", "test_article", "new content");
    return { success: true, data: response, name: "UPDATE Article" };
  } catch (error) {
    return { success: false, error: error, name: "UPDATE Article" };
  }
}

export async function testUploadMedia() {
  try {
    const buffer = await api.uploadMedia("workflow", "test_article", "videos", "video.heif", new File([""], "video.heif", { type: "video/heif" }));
    return { success: true, data: buffer, name: "UPLOAD Media" };
  } catch (error) {
    return { success: false, error: error, name: "UPLOAD Media" };
  }
}

export async function testGetVideo() {
  try {
    const media = await api.getMedia("workflow", "test_article", "videos", "video.heif");
    return { success: true, data: media,  name: "GET Media" };
  } catch (error) {
    console.log(error)
    return { success: false, error: error, name: "GET Media" };
  }
}

export async function testGetArticle() {
  try {
    const article = await api.getArticle("workflow", "test_article");
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
    const response = await api.deleteMedia("workflow", "test_article", "videos", "video.heif");
    return { success: true, data: response, name: "DELETE Media" };
  } catch (error) {
    return { success: false, error: error, name: "DELETE Media" };
  }
}

export async function testDeleteArticle() {
  try {
    const response = await api.deleteArticle("workflow", "test_article");
    return { success: true, data: response, name: "DELETE Article" };
  } catch (error) {
    return { success: false, error: error, name: "DELETE Article" };
  }
}
