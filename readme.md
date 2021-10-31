# Python Websocket Example

A simple example project for using websockets to call python functions from javascript. 

## Instructions

### Running The Example

1. Clone the repository and open terminal in the folder
2. Run `python -m pip install -r requirements.txt`
3. Run `python __main__.py`
4. Open http://127.0.0.1:8000/ in your browser
5. Follow the instructions on the website

### Defining new functions

All functions that you can call from javascript are defined in `api.py`.

### Calling functions

If the function defined in python looks like this
```python
def add(a, b):
    return a + b
```

Then it can be called in javascript like this

```js
let resultPromise = api.add(4,5);
```

The result is a [promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), so you should either
call the function from inside an `async` function with `await`, like this:

```js
async function myFunction() {
    const result = await api.add(4,5);
    console.log(`The result was ${result}`)
}

myFunction() 
```
Or by calling `.then` on the promise with a callback.

```js 
api.add(4,5).then(result=>console.log(`The result was ${result}`))
```

