const form = document.getElementById("write-form");

const handleSubmitForm = async (event) => {
  event.preventDefault();

  const body = new FormData(form);

  //세계시간 기준으로 보내게 됨.
  body.append("insertAt", new Date().getTime());
  /*이벤트가 동작하지 않게 막음*/
  try {
    const res = await fetch("/items", {
      method: "POST",
      body,
    });
    const data = await res.json();
    if (data === "200") window.location.pathname = "/";
  } catch (e) {
    console.error(e);
  }

  console.log();
};

form.addEventListener("submit", handleSubmitForm);
