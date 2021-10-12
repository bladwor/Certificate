window.addEventListener("load", (event) => {
			// **** NAV MENU ****
			let menuTimeoutIDs = [];
			const sublinks = document.querySelectorAll(".submenu");
			sublinks.forEach((link) => {
				link.addEventListener("mouseenter", (event) => {
					if (window.innerWidth > 990) {
						menuTimeoutIDs.forEach(window.clearTimeout);
						sublinks.forEach((link) => link.classList.remove("open"));
						event.target.classList.add("open");
					}
				});
				link.addEventListener("mouseleave", (event) => {
					if (window.innerWidth > 990) {
						const isMenuLink = event.relatedTarget.classList.contains("menu-link");
						if (isMenuLink && event.relatedTarget.getAttribute("href")) {
							return event.target.classList.remove("open");
						}
						const timeoutID = setTimeout(() => {
							event.target.classList.remove("open");
						}, 1000);
						menuTimeoutIDs.push(timeoutID);
					}
				});
				link.addEventListener("click", (event) => {
					if (window.innerWidth <= 990) {
						event.target.closest("li.submenu").classList.add("open");
					}
				});
			});
			document.querySelector(".burger").addEventListener("click", (event) => {
				document.querySelector(".wrapper").classList.toggle("open");
				document.querySelector(".burger").classList.toggle("is-active");
			});
			document.querySelectorAll(".close-submenu").forEach((item) => {
				item.addEventListener("click", (event) => {
					event.preventDefault();
					event.stopPropagation();
					event.target.closest("li.open").classList.remove("open");
				});
			});
			// const firstName = document.querySelectorAll("#firstName");
			// const lastName = document.querySelectorAll("#lastName");
			// const clienId = document.querySelectorAll("#clienId");
			// const inputValue =  document.addEventListener("oninput", (event) => {
			// })
			//   let concatInputValue = firstName.value + " " + lastName.value;
			//   clienId.value = concatInputValue;
			firstName.oninput = function(event) {
				clientId.value = event.target.value + " " + lastName.value;
			};
			lastName.oninput = function(event) {
				clientId.value = firstName.value + " " + event.target.value;
			};
		});