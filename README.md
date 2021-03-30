# Developing a plugin framework with `pluggy`

Repo to experiment and learn how plugins can be implemented with [pluggy](https://pluggy.readthedocs.io/en/latest/).

## How Plugins work

Plugins, in general, provide the ability to extend or modify the behavior of a `host program` by installing a `plugin` for that program. Plugins allow you extend an application by using hook functions that are implemented in plugins and that can be dynamically loaded. The host program calls these hooks to provide functionality.

Components of a plugin architecture:

* `host` or `host program` - the program offering extensibility by specifying hook functions and invoking their implementation(s) as part of program execution. core system and application entry point
* `plugin` - the program implementing (a subset of) the specified hooks and participating in program execution when the implementations are invoked by the host

### Pluggy

`pluggy` is a Python library that provides the core of plugin management for `pytest`.

Components of `pluggy`:

* **Hook Specification** - blue print that the plugin manager understands about the plugin definitions. Hook specifications have no code. `host_`-prefix is the typical naming convention, but not necessary.
* **Plugin** - The actual implementation of hook functions based based on the hookspecs.
* **Plugin Manager** - The plugin manager is responsible for finding and registering plugins
* **Hook Implementation** - actual implementation of a hook

#### Collecting results

`pluggy` hook calls are `1:N` , meaning that, by default, calling a hook results in all underlying hook implementation functions to be invoked in sequence via a loop. Any function which returns a value other then a `None` result will have that result appended to a [`list`](https://docs.python.org/3/library/stdtypes.html#list) which is returned by the call. The `None` return values are essentially is "swallowed."

The exception to this behavior is if the hook has been marked to return its [first result only](https://pluggy.readthedocs.io/en/latest/#firstresult) in which case only the first single value (which is not `None`) will be returned.

#### Advanced Features of `pluggy`

* [setuptools entrypoints](https://pluggy.readthedocs.io/en/latest/index.html?highlight=setuptools#loading-setuptools-entry-points)
* [hook ordering](https://pluggy.readthedocs.io/en/latest/index.html?highlight=hook%20order#call-time-order)
* [hookwrapping](https://pluggy.readthedocs.io/en/latest/index.html?highlight=Wrappers#wrappers)
* plugins defining new hooks

#### Benefits of `pluggy`

* hooks can evolve
  * new arguments do not affect plugins
* no state or behavior
  * plugins are free to keep state

## Sample Application

For our sample application, we're developing a CLI application using `Click` that will allow us to easily process different input file formats. Our CLI app will implement three different plugins to support `yaml`, `json`, and `csv` file types.

[Initial Commit](../../tree/917b6868d3ae88f1e20c7d42cdc17d524556581d/)

[Adding Skeleton CLI app](../../tree/e96f55a489ac49713f13a7671dffad8078fbc612/)

[Defining the hook specification](../../tree/02839cbf15f906b88b409d53bc9d8799d0ee9d71/)

[Adding the YAML reader plugin](../../tree/af15924a080aa97ff30fc157183cc7df9587c9d2/)

[Implementing the Plugin Manager and calling the hook from the host program](../../tree/e6754a4d733794367b55df92080073a5fcdc5f2f/)

[Adding additional plugins](../../tree/4d5b36d67665b8169b58fa1d7e46883c69b24352/)
