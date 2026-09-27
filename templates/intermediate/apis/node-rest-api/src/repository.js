let items = [
  { id: 1, name: "Example item" }
];

export function listItems() {
  return [...items];
}

export function createItem(name) {
  const item = { id: Date.now(), name };
  items.push(item);
  return item;
}

export function findItem(id) {
  return items.find(item => item.id === Number(id)) ?? null;
}
