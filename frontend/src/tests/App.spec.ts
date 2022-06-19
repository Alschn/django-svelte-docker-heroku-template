import {render} from '@testing-library/svelte';
import App from "../App.svelte";


test("should render App", () => {
  const component = render(App);
  expect(() => component.getByText('Hello Svelte!')).not.toThrow();
});
