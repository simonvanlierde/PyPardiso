# coding: utf-8
import pytest

from pypardiso.pardiso_wrapper import PyPardisoSolver, _load_mkl_rt


def test_mkl_rt_lookup_runs_once():
    _load_mkl_rt.cache_clear()
    first, second = PyPardisoSolver(), PyPardisoSolver()
    assert first.libmkl is second.libmkl
    assert _load_mkl_rt.cache_info().misses == 1


def test_mkl_rt_env_var_set_later_is_used(monkeypatch):
    PyPardisoSolver()  # the search result is cached now
    monkeypatch.setenv('PYPARDISO_MKL_RT', '/nonexistent/libmkl_rt.so')
    with pytest.raises(OSError):
        PyPardisoSolver()
