import { page } from "../store";
import { deleteAllCookies, getCookieValue } from "./shenanigans";

var theme: string;

if (window.matchMedia) {
  if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
    theme = "light";
  } else {
    theme = "dark";
  }
}

const functions = {

  auth: () => {

  },
  Foo: () => {
    page.set("Foo")
  },
  Home: () => {
    page.set("Home")
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
      .then(() => console.log(`Color ${color} copied to clipboard`))
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
