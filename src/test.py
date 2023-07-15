from litely import Litely

current_version = "0.0.3"

updater = Litely(current_version)
updater.check_for_updates("RuskyDev/ruskydev.github.io")
