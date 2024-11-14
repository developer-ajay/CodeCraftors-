
"""
10. Hard: Implement a class hierarchy for a plugin system with:
- Abstract base class 'Plugin'
- Metaclass 'PluginMeta' for registration
- Plugin loader class 'PluginLoader'
Plugins should be automatically registered when defined and loadable by name.
"""
import unittest
import math
class PluginMeta(type):
    pass

class Plugin(metaclass=PluginMeta):
    pass

class PluginLoader:
    pass

# Example plugins
class AudioPlugin(Plugin):
    pass

class VideoPlugin(Plugin):
    pass

class TestPluginSystem(unittest.TestCase):
    def test_plugin_system(self):
        loader = PluginLoader()
        self.assertEqual(len(loader.get_available_plugins()), 2)
        
        audio_plugin = loader.load_plugin("AudioPlugin")
        self.assertIsInstance(audio_plugin, AudioPlugin)
        
        video_plugin = loader.load_plugin("VideoPlugin")
        self.assertTrue(video_plugin.is_compatible())

if __name__ == "__main__":
    unittest.main()
