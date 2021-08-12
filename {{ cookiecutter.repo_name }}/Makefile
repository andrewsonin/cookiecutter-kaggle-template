.PHONY: requirements dirs init config push pull clean_remote

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
requirements: 
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Create directory structure for data and models
dirs:
	mkdir -p models data/external data/interim data/processed data/raw

## Download and deploy Kaggle input data
download:
	kaggle competitions download -c '{{ cookiecutter.repo_name }}' -p 'input/{{ cookiecutter.repo_name }}'
	unzip 'input/{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}.zip' -d 'input/{{ cookiecutter.repo_name }}' && rm 'input/{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}.zip'

## Initialize git and (optionally) DVC
init:
	git init
	{% if cookiecutter.use_dvc == 'yes' -%}
	dvc init
	{% endif %}

## Configure initial git/DVC/remote settings
config:
	dvc config core.analytics false
	{% if ((cookiecutter.use_dvc == 'yes') and (cookiecutter.remote_storage == 'hdfs')) -%}
	hdfs dfs -mkdir -p {{ cookiecutter.hdfs_url }}/{{ cookiecutter.module_name }}
	dvc remote add -d -f storage {{ cookiecutter.hdfs_url }}/{{ cookiecutter.module_name }}
	{% endif %}
	{% if ((cookiecutter.use_dvc == 'yes') and (cookiecutter.remote_storage == 's3')) -%}
	dvc remote add -d -f storage {{ cookiecutter.s3_bucket }}/{{ cookiecutter.module_name }}
	dvc remote modify storage endpointurl {{ cookiecutter.s3_endpoint }}
	{% endif %}

## Initialize poetry environment
poetry:
	poetry update -vvv

## Install python source files from the input/src/{{ cookiecutter.module_name }} as a module in edit mode
pymodule:
	pip install -e input/src

## Push changes to git and (optionally) DVC remotes
push:
	git push -u origin $(branch)
	{% if cookiecutter.use_dvc == 'yes' -%}
	dvc push
	{% endif %}

## Pull changes from git and (optionally) DVC remotes
pull:
	git pull origin $(branch)
	{% if cookiecutter.use_dvc == 'yes' -%}
	dvc pull
	{% endif %}
	
## Remove project folder from configured remote
clean_remote:	
	{% if ((cookiecutter.use_dvc == 'yes') and (cookiecutter.remote_storage == 'hdfs')) -%}
	hdfs dfs -rm -r -skipTrash {{ cookiecutter.hdfs_url }}/{{ cookiecutter.module_name }}
	{% endif %}
	{% if ((cookiecutter.use_dvc == 'yes') and (cookiecutter.remote_storage == 's3')) -%}
	aws s3 rm {{ cookiecutter.s3_bucket }}/{{ cookiecutter.module_name }} --recursive --endpoint-url {{ cookiecutter.s3_endpoint }}
	{% endif %}
	
#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
