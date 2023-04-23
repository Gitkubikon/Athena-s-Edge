<script>
  import { api } from "../main";
  import { content, page } from "../store";
  import { onUltraMount } from "../utils/shenanigans";

  export let upload_date = "";
  export let name = "";
  export let description = "";
  export let imgSrc = "";
  export let dislikes = "";
  export let main_tag = "";
  export let likes = "";
  export let bgSrc = "";
  let card__image;

  onUltraMount(() => {
    card__image.style.background = `${bgSrc}`;
  });
</script>

<div
  on:keydown={() => {}}
  on:click={async () => {
    content.set(await api.getArticle(main_tag, name));
    page.set("Article")
  }}
  class="card"
>
  <div bind:this={card__image} class="card__image">
    <img src={imgSrc} alt={imgSrc} />
  </div>
  <div class="card__upload_date">{upload_date}</div>
  <div class="card__unit-name">{name}</div>
  <div class="card__unit-description">{description}</div>

  <div class="card__unit-stats clearfix">
    <div class="one-third">
      <div class="stat">{dislikes}<sup>S</sup></div>
      <div class="stat-value">dislikes</div>
    </div>

    <div class="one-third">
      <div class="stat">{main_tag}</div>
      <div class="stat-value">main_tag</div>
    </div>

    <div class="one-third no-border">
      <div class="stat">{likes}</div>
      <div class="stat-value">likes</div>
    </div>
  </div>
</div>

<style>
  *,
  *:before,
  *:after {
    box-sizing: border-box;
  }

  .card {
    background: var(--ctp-base);
    width: 300px;
    display: inline-block;
    margin: 25px;
    border-radius: 19px;
    position: relative;
    text-align: center;
    box-shadow: -1px 15px 30px -12px black;
    z-index: 9999;
  }

  .card:hover {
    transform: translateY(-0.25rem);
  }

  .card__image {
    position: relative;
    height: 230px;
    margin-bottom: 35px;
    border-top-left-radius: 14px;
    border-top-right-radius: 14px;
  }

  .card__image {
    /* background: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/195612/barbarian-bg.jpg"); */
  }

  .card__image img {
    width: 400px;
    position: absolute;
    top: -65px;
    left: -70px;
  }

  .card__upload_date {
    text-transform: uppercase;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 3px;
  }

  .card__upload_date {
    color: var(--ctp-teal);
  }

  .card__unit-name {
    font-size: 26px;
    color: var(--ctp-text);
    font-weight: 900;
    margin-bottom: 5px;
  }

  .card__unit-description {
    padding: 20px;
    margin-bottom: 10px;
  }

  .card__unit-stats {
    background: var(--ctp-teal);
  }
  .card__unit-stats .one-third {
  }

  .card__unit-stats {
    color: var(--ctp-mantle);
    font-weight: 700;
    border-bottom-left-radius: 14px;
    border-bottom-right-radius: 14px;
  }
  .card__unit-stats .one-third {
    width: 33%;
    float: left;
    padding: 20px 15px;
  }
  .card__unit-stats sup {
    position: absolute;
    bottom: 4px;
    font-size: 45%;
    margin-left: 2px;
  }
  .card__unit-stats .stat {
    position: relative;
    font-size: 24px;
    margin-bottom: 10px;
  }
  .card__unit-stats .stat-value {
    text-transform: uppercase;
    font-weight: 400;
    font-size: 12px;
  }
  .card__unit-stats .no-border {
    border-right: none;
  }

  .clearfix:after {
    visibility: hidden;
    display: block;
    font-size: 0;
    content: " ";
    clear: both;
    height: 0;
  }
</style>
