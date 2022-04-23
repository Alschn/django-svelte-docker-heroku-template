<script lang="ts">
  let count: number = 0;
  const increment = () => count += 1;
  const decrement = () => count -= 1;
</script>

<section>
  <h1>Hello Svelte!</h1>

  <p>
    This is an example of Svelte app rendered into div in Django HTML.
    You can treat it like a component.
  </p>

  <p>
    Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn
    how to build Svelte apps
  </p>

  <p>Count: {count}</p>

  <div class="buttons">
    <button on:click={increment}>+</button>
    <button on:click={decrement}>-</button>
  </div>
</section>

<style lang="scss">
  $title-color: #ff3e00;

  * {
    font-family: Menlo, Monaco, Consolas, "Courier New", monospace;
  }

  section {
    text-align: center;
    border: 1px solid black;

    h1 {
      color: $title-color;
      text-transform: uppercase;
      font-size: 4em;
      font-weight: 100;
    }
  }

  .buttons {
    margin: 4px;

    button {
      padding: 4px 8px;
    }
  }
</style>
