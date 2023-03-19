import {expect, it} from "vitest";
import {render, screen} from "@testing-library/svelte";
import App from "../components/App.svelte";

it("should render App", () => {
  render(App);
  expect(screen.getByText("Hello Svelte!")).toBeInTheDocument();
});
