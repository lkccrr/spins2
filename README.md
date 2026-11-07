[![spins2](https://img.shields.io/pypi/v/spins2?style=flat-square)](https://pypi.org/project/spins2/)
[![spins2](https://img.shields.io/pypi/pyversions/spins2?style=flat-square)](https://pypi.org/project/spins2/)
[![spins2](https://img.shields.io/pypi/l/spins2?style=flat-square)](https://pypi.org/project/spins2/)
[![spins2](https://img.shields.io/pypi/dm/spins2?style=flat-square)](https://pypi.org/project/spins2/)
[![spins2](https://img.shields.io/pypi/wheel/spins2?style=flat-square)](https://pypi.org/project/spins2/)
[![mcta](https://img.shields.io/github/last-commit/lkccrr/mcta?style=flat-square)](https://github.com/lkccrr/mcta)
[![mcta](https://img.shields.io/github/release-date/lkccrr/mcta?style=flat-square)](https://github.com/lkccrr/mcta)

# spins2

> **Deprecated — no longer maintained.**
> Everything `spins2` used to do now lives in
> [**mcta**](https://github.com/lkccrr/mcta) (Meta Crystal Toolkit & Analysis),
> as the `mt.mc` command.

`spins2` is kept on PyPI only so that existing environments break loudly instead
of silently running stale code. Since 0.0.4 the distribution ships no code at all:
`import spins2` raises `ImportError` with a pointer to the replacement.

## Migrate

```bash
pip install "mcta[mc]"   # mt.mc needs numba
mt.mc --help
```

## Links

- New project: <https://github.com/lkccrr/mcta> · <https://pypi.org/project/mcta/>
- This repository (archived): <https://github.com/lkccrr/spins2>

## License

MIT
