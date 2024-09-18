<script>
  import { getDatabase, ref, push } from "firebase/database";
  import Footer from "../components/Nav.svelte";
  import {
    getStorage,
    ref as refImage,
    uploadBytes,
    getDownloadURL,
  } from "firebase/storage";
  import Nav from "../components/Nav.svelte";

  let title;
  let price;
  let description;
  let place;
  let files;
  const storage = getStorage();
  const db = getDatabase();

  function writeUserData(imgUrl) {
    push(ref(db, "items/"), {
      title,
      price,
      description,
      place,
      insertAt: new Date().getTime(),
      imgUrl,
    });
    alert("글쓰기가 완료되었습니다.");
    window.location.hash = "/";
  }

  const uploadFile = async () => {
    const file = files[0];
    const name = file.name;
    const imgRef = refImage(storage, name);
    await uploadBytes(imgRef, file);
    const url = await getDownloadURL(imgRef);
    return url;
  };

  const handelSubmit = async () => {
    const url = await uploadFile();
    writeUserData(url);
  };
</script>

<!-- event.preventDefault()와 같음-->
<form
  id="write-form"
  on:submit|preventDefault={handelSubmit}
  action="/items"
  method="POST"
>
  <div>
    <label for="image">이미지</label>
    <input type="file" id="id" bind:files name="image" required />
  </div>
  <div>
    <label for="title">제목</label>
    <input type="text" id="title" name="title" required bind:value={title} />
  </div>
  <div>
    <label for="price">가격</label>
    <input type="number" id="price" name="price" required bind:value={price} />
  </div>
  <div>
    <label for="description">설명</label>
    <input
      type="text"
      id="description"
      name="description"
      required
      bind:value={description}
    />
  </div>
  <div>
    <label for="place">장소</label>
    <input type="text" id="place" name="place" required bind:value={place} />
  </div>
  <div>
    <button class="write-button" type="submit">글쓰기!</button>
  </div>
  <div id="info"></div>
</form>

<Nav location="write" />

<style>
  .write-button {
    background-color: tomato;
    margin: 10px;
    border-radius: 10px;
    padding: 5px 12px 5px 12px;
    color: white;
    cursor: pointer;
  }
</style>
