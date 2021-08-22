const url = 'ws://localhost:8000/ws/chat/'
const ws = new WebSocket(url)
ws.onopen = (event) => {
    console.log("connection is opened");
}

ws.onmessage = (event) => {
    console.log(event);
    console.log("Message is received");
}

ws.onclose = (event) => {
    console.log("Connection is closed");
}

ws.onerror = (event) => {
    console.log("Something went wrong");
}