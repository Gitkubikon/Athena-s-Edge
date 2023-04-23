import { page, testApiDivs } from "../store";
import { deleteAllCookies, deleteCookie, getCookieValue } from "./shenanigans";
import {
  testCreateArticle,
  testUpdateArticle,
  testUploadMedia,
  testGetArticle,
  testGetVideo,
  testGetArticleMetadata,
  testDeleteMedia,
  testDeleteArticle
} from "./testapi";

var theme: string;

if (window.matchMedia) {
  if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
    theme = "light";
  } else {
    theme = "dark";
  }
}


const functions = {

  Foo: () => {
    page.set("Foo")
  },
  Home: () => {
    page.set("Home")
  },
  Article: () => {
    page.set("Article")
  },
  AdminPage: () => {
    page.set("AdminPage")
  },
  ArticleForm: () => {
    page.set("ArticleForm")
  },
  StyleGuide: () => {
    page.set("StyleGuide")
  },
  Logout: () => {
    deleteCookie("token")
    page.set("Foo")
  },
  TestApi: async () => {

    const testFunctions = {
      testCreateArticle,
      testUpdateArticle,
      testUploadMedia,
      testGetArticle,
      testGetVideo,
      testGetArticleMetadata,
      testDeleteMedia,
      testDeleteArticle,
    };

    const testResults = {};

    for (const [key, value] of Object.entries(testFunctions)) {
      const result = await value();
      testResults[key] = result;
    }

    for (const [key, result] of Object.entries(testResults)) {
      const headerDiv = document.createElement("div");
      const contentDiv = document.createElement("div");

      headerDiv.innerText = `Test: ${key}`;
      contentDiv.style.display = "block";

      if (result.success) {
        headerDiv.classList.add("test-header", "test-success");
        headerDiv.innerHTML = `${result.name} Succeeded!`;
        // contentDiv.innerHTML = `<pre>Data: ${formatJson(result.data)}</pre>`;
        // contentDiv.appendChild(jsonToHtml(result))
      } else {
        headerDiv.classList.add("test-header", "test-failure");
        headerDiv.innerHTML = `${result.name} Failed!`;
        // contentDiv.innerHTML = `<pre>Error: ${formatJson(result.error)}</pre>`;
        contentDiv.appendChild(jsonToHtml(result));
        // console.log(result.error)
      }

      headerDiv.addEventListener("click", () => {
        contentDiv.style.display = contentDiv.style.display === "none" ? "block" : "none";
      });

      testApiDivs.update((divs) => [...divs, headerDiv, contentDiv]);
    }

    function jsonToHtml(json) {
      const container = document.createElement('div');
      for (const key in json) {
        if (json.hasOwnProperty(key)) {
          const value = json[key];
          const valueType = typeof value;
          const item = document.createElement('div');
          item.innerHTML += `<strong>${key}:</strong> `;

          if (key === "stack") {
          } else {
            if (value === null) {
              item.innerHTML += 'null';
              item.classList.add('json-null');
            } else if (valueType === 'object') {
              item.classList.add('json-object');
              const subContainer = jsonToHtml(value);
              subContainer.style.display = 'none';
              item.appendChild(subContainer);
            } else {
              item.innerHTML += value;
              item.classList.add(`json-${valueType}`);
            }
          }

          container.appendChild(item);
        }
      }
      return container;
    }






    // function jsonToHtml(json) {
    //   const container = document.createElement('div');
    //   for (const key in json) {
    //     if (json.hasOwnProperty(key)) {
    //       const value = json[key];
    //       const valueType = typeof value;
    //       const item = document.createElement('div');
    //       // const button = document.createElement('div'); // Add a new button
    //       // button.innerHTML = '-'; // Set the initial label of the button
    //       // button.classList.add('ultrafocus'); // Add a class to the button for styling
    //       // button.classList.add('button'); // Add a class to the button for styling
    //       // item.appendChild(button); // Add the button to the item div
    //       item.innerHTML += `<strong>${key}:</strong> `; // Add the rest of the item content
    //       if (value === null) {
    //         item.innerHTML += 'null';
    //         item.classList.add('json-null');
    //       } else if (valueType === 'object') {
    //         item.classList.add('json-object');
    //         const subContainer = jsonToHtml(value);
    //         subContainer.style.display = 'none'; // Set the subContainer to be hidden by default
    //         item.appendChild(subContainer);

    //         // Create an on:click function for the button
    //         // button.onclick = () => {
    //         //   if (subContainer.style.display === 'none') {
    //         //     subContainer.style.display = 'block'; // Toggle display property
    //         //     button.innerHTML = '-';
    //         //   } else {
    //         //     subContainer.style.display = 'none'; // Toggle display property
    //         //     button.innerHTML = '+';
    //         //   }
    //         // };
    //       } else {
    //         item.innerHTML += value;
    //         item.classList.add(`json-${valueType}`);
    //       }
    //       container.appendChild(item);
    //     }
    //   }
    //   return container;
    // }













  },
  // lock: () => {
  //   lock()
  // },

  copyColor: () => {
    const trailerElement = document.getElementById("trailer");
    const rect = trailerElement.getBoundingClientRect();
    const x = rect.left + rect.width / 2;
    const y = rect.top + rect.height / 2;
    const elements: Element[] = Array.from(document.elementsFromPoint(x, y));
    const divElements: HTMLDivElement[] = elements.filter(
      (el) => el.tagName === "DIV"
    ) as HTMLDivElement[];
    const element = divElements[0];

    const color = window.getComputedStyle(element).backgroundColor;
    navigator.clipboard
      .writeText(color)
      .then(() => alert(`Color ${color} copied to clipboard`))
      .catch((error) =>
        console.error(`Error copying color to clipboard: ${error}`)
      );
  },

  // toggleMobileNav: () => {
  //   toggleMobileNav()

  //   const sidenav = document.getElementById("sidenav")
  //   const contrarotate = document.getElementById("contrarotate")
  //   mobile.subscribe((mobile) => {
  //     console.log(sidenav)
  //     if (mobile.valueOf()) {
  //       sidenav.style.boxShadow = "-10px -10px 1000px 1000px rgba(0, 0, 0, 0.5)";
  //       sidenav.style.transform = 'rotate(8deg)';
  //       sidenav.style.height = '110vh';
  //       contrarotate.style.transform = 'rotate(-8deg)';
  //       contrarotate.style.left = "106px";
  //       sidenav.style.width = '180px';
  //       for (var i = 0; i < sidenav.children.length; i++) {
  //         //@ts-ignore
  //         sidenav.children[i].style.width = '60px';
  //       }
  //       // Add CSS transitions
  //       sidenav.style.transition = 'transform 0.5s ease, width 0.5s ease';
  //       contrarotate.style.transition = 'left 0.5s ease, opacity 0.5s ease 0.5s';
  //       contrarotate.style.opacity = '1';
  //     } else {
  //       sidenav.style.boxShadow = "0 0 0px 0px rgba(0, 0, 0, 0.5)";
  //       sidenav.style.transform = 'rotate(0deg)';
  //       // contrarotate.style.transform = 'rotate(0deg)';
  //       contrarotate.style.left = "-56px";
  //       sidenav.style.width = '0px';
  //       for (var i = 0; i < sidenav.children.length; i++) {
  //         //@ts-ignore
  //         sidenav.children[i].style.width = '0px';
  //       }
  //       // Add CSS transitions
  //       sidenav.style.transition = 'transform 0.5s ease, width 0.5s ease';
  //       contrarotate.style.transition = 'left 0.5s ease, opacity 0.5s ease';
  //       contrarotate.style.opacity = '0';

  //     }
  //     // Add CSS transition for contra rotate appearing
  //     contrarotate.style.transition = 'left 0.5s ease, opacity 0.5s ease 0.5s, transform 0s ease';
  //   })
  // },

  toggleTheme: () => {
    document.documentElement.classList.toggle(theme);
    var themeDiv = document.querySelector('.theme');
    themeDiv!.classList.toggle('checked');
  },
  // mobilenav: () => {
  //   const sideNavElement = document.querySelector('.sidenav') as HTMLElement;
  //   sideNavElement.style.transition = "left 0.3s ease-in-out";
  //   const width = sideNavElement.style.left;
  //   if (sideNavElement && width === "0px") {
  //     sideNavElement.style.left = "-60px";
  //   } else {
  //     sideNavElement.style.left = "0";
  //   }
  // }
};

export { functions }
