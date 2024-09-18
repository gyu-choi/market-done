<script lang="ts">
  import { onMount } from "svelte";
  import Footer from "../components/Nav.svelte";
  import { getDatabase, ref, onValue } from "firebase/database";
  import Nav from "../components/Nav.svelte";

  let hour = new Date().getHours();
  let min = new Date().getMinutes();

  // 반응형 변수
  $: items = [];

  const calcTime = (timestamp) => {
    /* UTC로 보내주고 한국시간을 빼기 때문에 발생하는 9시간을 빼줌*/
    const curTime = new Date().getTime() - 9 * 60 * 60 * 1000;
    const time = new Date(curTime - timestamp);
    const hour = time.getHours();
    const minutes = time.getMinutes();
    const second = time.getSeconds();

    if (hour > 0) return `${hour}시간 전`;
    else if (minutes > 0) return `${minutes}분 전`;
    else if (second > 0) return `${second}초 전`;
    else return "방금 전";
  };

  const db = getDatabase();
  const itemsRef = ref(db, "items/");

  onMount(() => {
    onValue(itemsRef, (snapshot) => {
      const data = snapshot.val();
      items = Object.values(data).reverse();
    });
  });
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
  {#each items as item}
    <div class="item-list">
      <div class="item-list__img">
        <img alt={item.title} src={item.imgUrl} />
      </div>
      <div class="item-list__info">
        <div class="item-list__info-title">{item.title}</div>
        <div class="item.list__info-meta">
          {item.place}
          {calcTime(item.insertAt)}
        </div>
        <div class="item.list__info-price">{item.price}</div>
        <div>{item.description}</div>
      </div>
    </div>
  {/each}

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

<Nav location="home" />
