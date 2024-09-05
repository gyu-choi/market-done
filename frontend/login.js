const form = document.querySelector("#login-form");

let accessToken = null;

const handleSubmit = async (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const sha256Password = await sha256(formData.get("password").toString());
  formData.set("password", sha256Password);

  console.log(formData);
  console.log([...formData.entries()]);

  const res = await fetch("/login", {
    method: "POST",
    body: formData,
    headers: {
      Accept: "application/json",
    },
  });

  const data = await res.json();
  accessToken = data.access_token;

  const infoDiv = document.querySelector("#info");
  infoDiv.innerText = "로그인되었습니다.";

  const btn = document.createElement("button");
  btn.innerText = "상품 가져오기";
  btn.addEventListener("click", async () => {
    const res = await fetch("/items", {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });

    const data = (await res).json();

    console.log(data);
  });
  infoDiv.appendChild(btn);

  if (res.status == 200) {
    alert("로그인에 성공했습니다!!");
    // window.location.pathname = "/";
    console.log(res.status);
  } else if (res.status == 401) {
    alert("id 혹은 password가 틀렸습니다.");
  }
};

form.addEventListener("submit", handleSubmit);
