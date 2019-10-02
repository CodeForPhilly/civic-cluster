# civic-cloud

## Exposing Websites

We have `*.beta-cluster.phl.io` pointing at the Linode NodeBalancer for the cluster via DNS.

To expose a web application through this interface with HTTPS, define an Ingress that looks like this:

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: myapp
  namespace: myapp
  labels:
    app: myapp
  annotations:
    certmanager.k8s.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - myapp.beta-cluster.phl.io
    secretName: tls-secret
  rules:
  - host: myapp.beta-cluster.phl.io
    http:
      paths:
      - path: /
        backend:
          serviceName: myapp
          servicePort: 80
```

For an example, see [`platform/bitwarden/manifest.yaml`](./platform/bitwarden/manifest.yaml)
