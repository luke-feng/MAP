<template>
 <div id="wrapper">
   <div id="container" class= 'mid_404'>
    <p>
      <img src='@/assets/photo/404.png'>
    </p>
    <h2 class="title">Oops! It seems that this page does not exist.</h2>
   </div>
   <div id="footer">
      <div class="copyright" style="color:#459ead ">
          &copy; 2021
          <i class="fa fa-heart heart"></i> by SHINE
      </div>
   </div>
 </div>
</template>

<script>
export default {}
</script>
<style>
html,
body {
  margin: 0;
  padding: 0;
  height: 100%;
}
#wrapper {
  min-height: 100%;
  position: relative;
}
#container {
  padding: 10px;
  padding-bottom: 60px;
}
#footer {
  position: absolute;
  bottom: 0;
  width: 90%;
  height: 60px;
  text-align: right
}
.mid_404 {
  margin-top: 60px;
  max-width: 960px;
  margin-left: 30em;
  display: flex;
  flex-direction: column;
}
</style>
