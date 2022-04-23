<script>
  // you would unpack props this way:
  // export let prop1, prop2;

  // with $$props you can access all of the props passed to this component
</script>

<section>
  <h1>Hello 2nd Svelte app!</h1>

  <p>
    This is another Svelte app.
    You can render multiple of those in Django HTML.
  </p>

  <p>Props received from Django (retrieved from html source code):</p>

  <code>
    {JSON.stringify($$props)}
  </code>
</section>

<style lang="scss">
  * {
    font-family: Consolas, "Courier New", monospace;
  }

  section {
    margin-top: 8px;
    text-align: center;
    border: 1px solid #aaa;

    h1 {
      text-transform: uppercase;
      font-size: 3em;
      font-weight: 100;
    }
  }
</style>
