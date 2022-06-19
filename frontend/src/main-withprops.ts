import SecondApp from "./WithProps.svelte";

const app = new SecondApp({
  target: document.getElementById('secondary-svelte-app'),
  props: JSON.parse(document.getElementById('secondary-svelte-app-props').textContent),
});

export default app;
