async function loadProducts() {
  let res = await fetch('/api/products')
  let products = await res.json()

  let list = document.getElementById('list')
  list.innerHTML = ''
  for (let p of products) {
    let li = document.createElement('li')
    li.textContent = p.name + ' - ' + p.price + ' руб.'
    list.appendChild(li)
  }
}

document.getElementById('add').onclick = async function () {
  let name = document.getElementById('name').value
  let price = document.getElementById('price').value

  await fetch('/api/products', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: name, price: price })
  })

  document.getElementById('name').value = ''
  document.getElementById('price').value = ''
  loadProducts()
}

loadProducts()
