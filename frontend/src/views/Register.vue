<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <create-account-form data-background-color="green"> </create-account-form>
      </div>
    </div>
  </div>
</template>

<script>
import CreateAccountForm from '../views/Register/CreateAccountForm'
export default {
  components: {
    CreateAccountForm
  }
}
</script>
