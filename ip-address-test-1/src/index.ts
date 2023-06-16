addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const clientIP = request.headers.get("cf-connecting-ip")
  console.log(clientIP)
}
