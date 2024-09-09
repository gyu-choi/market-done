<script>
  let hour = new Date().getHours();
  let min = new Date().getMinutes();
</script>

<header>
  <div class="info-bar">
    <div class="info-bar__time">{hour}:{min}</div>
    <div class="info-bar__icons">
      <img src="assets/chart-bar.svg" alt="chart-bar" />
      <img src="assets/wifi.svg" alt="wifi" />
      <img src="assets/battery.svg" alt="battery" />
    </div>
  </div>
  <div class="menu-bar">
    <div class="menu-bar__location">
      <div>인계동</div>
      <div class="menu-bar__location-icon">
        <img src="assets/arrow-down.svg" alt="" />
      </div>
    </div>
    <div class="menu-bar__icons">
      <img src="assets/search.svg" alt="" />
      <img src="assets/menu.svg" alt="" />
      <img src="assets/alert.svg" alt=" " />
    </div>
  </div>
</header>
<main>
  <!-- <div class="item-list">
      <div class="item-list__img">
        <img src="css/assets/양파.jpg" alt="" />
      </div>
      <div class="item-list__info">
        <div class="item-list__info-title">양파 팝니다.</div>
        <div class="item-list__info-meta">인계동 1분 전</div>
        <div class="item-list__info-price">100원</div>
      </div>
    </div>
    <div class="item-list">
      <div class="item-list__img">
        <img src="css/assets/양파2.jpg" alt="" />
      </div>
      <div class="item-list__info">
        <div class="item-list__info-title">양파 입냄새 팝니다.</div>
        <div class="item-list__info-meta">인계동 2분 전</div>
        <div class="item-list__info-price">200원</div>
      </div>
    </div>
    <div class="item-list">
      <div class="item-list__img">
        <img src="css/assets/uni.jpg" alt="" />
      </div>
      <div class="item-list__info">
        <div class="item-list__info-title">유니 팝니다. 네고안됨</div>
        <div class="item-list__info-meta">인계동 10초전</div>
        <div class="item-list__info-price">199만원</div>
      </div>
    </div>
    <div class="item-list">
      <div class="item-list__img">
        <img src="css/assets/uni+양파.jpg" alt="" />
      </div>
      <div class="item-list__info">
        <div class="item-list__info-title">유니+양파 세트 팝니다.</div>
        <div class="item-list__info-meta">인계동 100초전</div>
        <div class="item-list__info-price">199만 100원</div>
      </div>
    </div>-->
  <a class="write-btn" href="#/Write">+ 글쓰기</a>
</main>
<footer>
  <div class="footer-block">
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/home.svg" alt="" />
      </div>
      <div>홈</div>
    </div>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/doc.svg" alt="" />
      </div>
      <div>동네생활</div>
    </div>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/location.svg" alt="" />
      </div>
      <div>내 근처</div>
    </div>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/chat.svg" alt="" />
      </div>
      <div>채팅</div>
    </div>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/user.svg" alt="" />
      </div>
      <div>나의 당근</div>
    </div>
  </div>
</footer>
