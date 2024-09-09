<form id="write-form" action="/items" method="POST">
  <div></div>
  <div>
    <label for="image">이미지</label>
    <input type="file" id="id" name="image" required />
  </div>
  <div>
    <label for="title">제목</label>
    <input type="text" id="title" name="title" required />
  </div>
  <div>
    <label for="price">가격</label>
    <input type="number" id="price" name="price" required />
  </div>
  <div>
    <label for="description">설명</label>
    <input type="text" id="description" name="description" required />
  </div>
  <div>
    <label for="place">장소</label>
    <input type="text" id="place" name="place" required />
  </div>
  <div>
    <button type="submit">글쓰기!</button>
  </div>
  <div id="info"></div>
</form>
