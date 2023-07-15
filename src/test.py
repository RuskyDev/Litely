from litely import Litely

current_version = "0.0.1"

updater = Litely(current_version)
updater.check_for_updates("RuskyDev/ruskydev.github.io")
