{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyO4h1w33qUH+LQJ8H+aFsH7",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ravitejanalla/RAVI/blob/master/Dwm1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UGzO10C1YbPO",
        "outputId": "1f42f0c3-09a5-484b-bd82-84855b6b46b0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "shape: (3, 3)\n",
            "dimensions: 2\n"
          ]
        }
      ],
      "source": [
        "\n",
        "import numpy as np\n",
        "#creation of multi-dimensional array\n",
        "a=np.array([[1,2,3],[2,3,4],[3,4,5]])\n",
        "#shape \n",
        "b=a.shape\n",
        "print(\"shape:\",b) #print(\"shape:\",a.shape)\n",
        "#dimension\n",
        "c=a.ndim\n",
        "print(\"dimensions:\",a.ndim) #print(\"dimensions:\",c)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "#creation of multi-dimensional array\n",
        "a=np.array([[1,2,3],[2,3,4],[3,4,5]])\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eGC_F7k6cU58",
        "outputId": "72f5f398-ceaf-4a99-a60e-6e3b43c53a18"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1 2 3]\n",
            " [2 3 4]\n",
            " [3 4 5]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#matrix full of zeros\n",
        "z=np.zeros((2,2))\n",
        "print(\"zeros:\",z)\n",
        "#matrix full of ones\n",
        "o=np.ones((2,2))\n",
        "print(\"ones:\",o) \n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R9ZLxjx6clR5",
        "outputId": "be26942d-ecb4-410d-b815-d2e47093ebab"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "zeros: [[0. 0.]\n",
            " [0. 0.]]\n",
            "ones: [[1. 1.]\n",
            " [1. 1.]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#matrix reshape\n",
        "a=np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])\n",
        "b=a.reshape(4,2,2)\n",
        "print(\"Original:\",a)\n",
        "print(\"Reshape:\",b)\n",
        "\n",
        "#matrix flatten\n",
        "c=a.flatten()\n",
        "print(\"flatten:\",c)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iTN0YM3_cpfC",
        "outputId": "7b4772d8-2b8d-4b51-d69d-47758a581472"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original: [[1 2 3 4]\n",
            " [2 3 4 5]\n",
            " [3 4 5 6]\n",
            " [4 5 6 7]]\n",
            "Reshape: [[[1 2]\n",
            "  [3 4]]\n",
            "\n",
            " [[2 3]\n",
            "  [4 5]]\n",
            "\n",
            " [[3 4]\n",
            "  [5 6]]\n",
            "\n",
            " [[4 5]\n",
            "  [6 7]]]\n",
            "flatten: [1 2 3 4 2 3 4 5 3 4 5 6 4 5 6 7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Appending data vertically\n",
        "x=np.array([[10,20],[80,90]])\n",
        "y=np.array([[30,40],[60,70]])\n",
        "v=np.vstack((x,y))\n",
        "print(\"vertically:\",v)\n",
        "#Appending data horizontally\n",
        "h=np.hstack((x,y))\n",
        "print(\"horizontally:\",h)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0EOM2hBrcu2R",
        "outputId": "cbfb854f-4cf2-41e7-f02d-13a7384d9031"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "vertically: [[10 20]\n",
            " [80 90]\n",
            " [30 40]\n",
            " [60 70]]\n",
            "horizontally: [[10 20 30 40]\n",
            " [80 90 60 70]]\n",
            "vertically: [[10 20]\n",
            " [80 90]\n",
            " [30 40]\n",
            " [60 70]]\n",
            "horizontally: [[10 20 30 40]\n",
            " [80 90 60 70]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#indexing\n",
        "a=np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])\n",
        "temp = a[[0, 1, 2, 3], [1, 1, 1, 1]]\n",
        "print(\"indexing\",temp)\n",
        "#slicing \n",
        "i=a[:4,::2]\n",
        "print(\"slicing\",i)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zvyRzfX2c7nR",
        "outputId": "e3dc68e9-605a-4e8b-fd7f-42d9e3962f58"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "indexing [2 3 4 5]\n",
            "slicing [[1 3]\n",
            " [2 4]\n",
            " [3 5]\n",
            " [4 6]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=np.array([[1,3,-1,4],[3,-2,1,4]])\n",
        "b=a.min()\n",
        "print(\"minimum:\",b)\n",
        "#max for finding maximum of an array\n",
        "c=a.max()\n",
        "print(\"maximum\",c)\n",
        "#mean\n",
        "a=np.array([1,2,3,4,5])\n",
        "d=a.mean()\n",
        "print(\"mean:\",d)\n",
        "#median\n",
        "e=np.median(a)\n",
        "print(\"median:\",e)\n",
        "#standard deviation\n",
        "f=a.std()\n",
        "print(\"standard deviation\",f)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Mo0K8hzydAW7",
        "outputId": "116ee14b-b5ae-4204-d40b-1b0b7330cee1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "minimum: -2\n",
            "maximum 4\n",
            "mean: 3.0\n",
            "median: 3.0\n",
            "standard deviation 1.4142135623730951\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import pandas as pd # importing pandas with alias pd. \n",
        "import io # io is a standard library no need to install it separately using pip\n",
        "from google.colab import files# files is an object obtaining from google.colab module\n",
        "uploaded = files.upload()# show the form to upload a file\n",
        "dataset = pd.read_excel(io.BytesIO(uploaded['Salary.xlsx'])) # performing input operation by accessing BytesIO module which is in io library.\n",
        "\n",
        "#dataset = pd.read_csv('Salary.csv') # to import the dataset into a variable\n",
        "#dataset = pd.read_excel('Salary.xlsx') # run pip install openpyxl to load excel file\n"
      ],
      "metadata": {
        "id": "6V9B5gN4q2yd",
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 90
        },
        "outputId": "e8ca8f08-7bc0-4971-88c7-d1d1529cb9f1"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-f8ec61a2-fbe0-4a94-ac3e-7eac42751a6b\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-f8ec61a2-fbe0-4a94-ac3e-7eac42751a6b\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving Salary.xlsx to Salary.xlsx\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X = dataset.iloc[:, :-1].values # attributes to determine independent variable / Class\n",
        "Y = dataset.iloc[:, -1].values # dependent variable / Class\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "ae1-NF3nrtOw"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "dataset = pd.read_excel('Salary.xlsx') \n",
        "num_var = dataset[['Age', 'Income']] #select numerical variables from dataset\n",
        "print(num_var) \n",
        "# impute the missing fields in a dataset using scikit-learn library’s SimpleImputer Class \n",
        "from sklearn.impute import SimpleImputer\n",
        "imp = SimpleImputer(missing_values=np.nan, strategy=\"mean\")\n",
        "X_mean = imp.fit_transform(num_var)# fit_transform method do calculating the mean of columns and then replacing the missing values according to it\n",
        "print(X_mean)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "52NPx8L2SoN2",
        "outputId": "2e22fca3-c461-4e8e-b101-6de78408f20e"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    Age   Income\n",
            "0  49.0  86400.0\n",
            "1  32.0  57600.0\n",
            "2  35.0  64800.0\n",
            "3  40.0  69600.0\n",
            "4  45.0      NaN\n",
            "5  40.0  69600.0\n",
            "6   NaN  62400.0\n",
            "7  53.0  94800.0\n",
            "8  55.0  99600.0\n",
            "9  42.0  80400.0\n",
            "[[4.90000000e+01 8.64000000e+04]\n",
            " [3.20000000e+01 5.76000000e+04]\n",
            " [3.50000000e+01 6.48000000e+04]\n",
            " [4.00000000e+01 6.96000000e+04]\n",
            " [4.50000000e+01 7.61333333e+04]\n",
            " [4.00000000e+01 6.96000000e+04]\n",
            " [4.34444444e+01 6.24000000e+04]\n",
            " [5.30000000e+01 9.48000000e+04]\n",
            " [5.50000000e+01 9.96000000e+04]\n",
            " [4.20000000e+01 8.04000000e+04]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd # importing pandas with alias pd. \n",
        "import io # io is a standard library no need to install it separately using pip\n",
        "from google.colab import files# files is an object obtaining from google.colab module\n",
        "uploaded = files.upload()# show the form to upload a file\n",
        "dataset = pd.read_excel(io.BytesIO(uploaded['Salary.xlsx'])) # performing input operation by accessing BytesIO module which is in io library.\n",
        "\n",
        "#dataset = pd.read_csv('Salary.csv') # to import the dataset into a variable\n",
        "#dataset = pd.read_excel('Salary.xlsx') # run pip install openpyxl to load excel file\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 90
        },
        "id": "Skb1_WPBBERK",
        "outputId": "7ef89908-d0c0-4a4c-dee7-fefedd2f0a58"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-6912d13a-6814-4ac6-b33d-adfe9bf91354\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-6912d13a-6814-4ac6-b33d-adfe9bf91354\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving Salary.xlsx to Salary (3).xlsx\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "_Nxjg1u2BOGK"
      },
      "execution_count": 41,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "dataset = pd.read_excel('Salary.xlsx') \n",
        "dataset.drop(['Region', 'OnlineShopper'], axis = 1, inplace = True) # .drop() method for deleting and filtering data frame\n",
        "\n",
        "dataset # display\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 363
        },
        "id": "s70JKfBqUPZ3",
        "outputId": "92e5f6cd-865e-4eb1-c992-a39ccb7334f5"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    Age   Income\n",
              "0  49.0  86400.0\n",
              "1  32.0  57600.0\n",
              "2  35.0  64800.0\n",
              "3  40.0  69600.0\n",
              "4  45.0      NaN\n",
              "5  40.0  69600.0\n",
              "6   NaN  62400.0\n",
              "7  53.0  94800.0\n",
              "8  55.0  99600.0\n",
              "9  42.0  80400.0"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-5eb8e0cd-b7ef-435b-9577-38ac44f3d417\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Age</th>\n",
              "      <th>Income</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>49.0</td>\n",
              "      <td>86400.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>32.0</td>\n",
              "      <td>57600.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>35.0</td>\n",
              "      <td>64800.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>40.0</td>\n",
              "      <td>69600.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>45.0</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>40.0</td>\n",
              "      <td>69600.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>NaN</td>\n",
              "      <td>62400.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>53.0</td>\n",
              "      <td>94800.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>55.0</td>\n",
              "      <td>99600.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>42.0</td>\n",
              "      <td>80400.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-5eb8e0cd-b7ef-435b-9577-38ac44f3d417')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-5eb8e0cd-b7ef-435b-9577-38ac44f3d417 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-5eb8e0cd-b7ef-435b-9577-38ac44f3d417');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import pandas as pd\n",
        "import io\n",
        "from google.colab import files\n",
        "uploaded = files.upload()\n",
        "dataset = pd.read_excel(io.BytesIO(uploaded['Salary.xlsx']))\n",
        "\n",
        "# Replacing column with mean of that column\n",
        "dataset['Age'] = dataset['Age'].fillna(dataset['Age'].mean())#fillna () method replaces the NULL values with mean\n",
        "dataset['Income'] = dataset['Income'].fillna(dataset['Income'].mean())\n",
        "\n",
        "# Replacing column with mode (number that occurs the most in a given list of numbers) of that column\n",
        "import statistics\n",
        "dataset['Age']=dataset['Age'].fillna(statistics.mode(dataset['Age']))\n",
        "dataset['Income']=dataset['Income'].fillna(statistics.mode(dataset['Income']))\n"
      ],
      "metadata": {
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 90
        },
        "id": "JEGplkcOWZV_",
        "outputId": "a71d09fa-0d26-46e9-d88d-1860bb6c5196"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-6cb7a0eb-cb53-400e-ba25-e2beb308f852\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-6cb7a0eb-cb53-400e-ba25-e2beb308f852\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving Salary.xlsx to Salary (1).xlsx\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np \n",
        "import math \n",
        "from sklearn.datasets import load_iris # loading iris dataset from sklearn datasets\n",
        "from sklearn import datasets, linear_model, metrics\n",
        " \n",
        "# load iris data set \n",
        "dataset = load_iris() \n",
        "a = dataset.data \n",
        "b = np.zeros(150) \n",
        " \n",
        "# take 1st column among 4 column of data set\n",
        "for i in range (150): \n",
        " b[i]=a[i,1] \n",
        " \n",
        "b=np.sort(b) #sort the array \n",
        " \n",
        "# create bins \n",
        "bin1=np.zeros((30,5))\n",
        "bin2=np.zeros((30,5)) \n",
        "bin3=np.zeros((30,5)) \n",
        "\n",
        "# Bin mean \n",
        "for i in range (0,150,5): #the sequence of the values from 0 to 149 gets created. But between each element will have a gap of ‘5’.\n",
        "    k=int(i/5) # int () function converts the specified value into an integer number\n",
        "    mean=(b[i] + b[i+1] + b[i+2] + b[i+3] + b[i+4])/5\n",
        "    for j in range(5): \n",
        "        bin1[k,j]=mean \n",
        "print(\"Bin Mean: \\n\",bin1) \n",
        " \n",
        "# Bin boundaries \n",
        "for i in range (0,150,5): \n",
        "    k=int(i/5) \n",
        "    for j in range (5): \n",
        "        if (b[i+j]-b[i]) < (b[i+4]-b[i+j]): \n",
        "            bin2[k,j]=b[i] \n",
        "        else: \n",
        "            bin2[k,j]=b[i+4] \n",
        "print(\"Bin Boundaries: \\n\",bin2) \n",
        " \n",
        "# Bin median \n",
        "for i in range (0,150,5): \n",
        "    k=int(i/5) \n",
        "    for j in range (5): \n",
        "        bin3[k,j]=b[i+2] \n",
        "print(\"Bin Median: \\n\",bin3)\n",
        "\n",
        "\n",
        "\n",
        "import numpy as np\n",
        "Data = np.array([[300,24],[200,21],[126,18],[567,27],[420,19],[189,30]])\n",
        "print (Data)\n",
        "\n",
        "from sklearn.preprocessing import MaxAbsScaler #Transform features by scaling each feature to a given range.\n",
        "from sklearn.preprocessing import MinMaxScaler\n",
        "\n",
        "MMS_scaler_model = MinMaxScaler()\n",
        "MMS_scaler_model.fit(Data)\n",
        "\n",
        "MAS_scaler_model = MaxAbsScaler()\n",
        "MAS_scaler_model.fit(Data)\n",
        "\n",
        "MMS_scaled_data = MMS_scaler_model.transform(Data)\n",
        "MAS_scaled_data = MAS_scaler_model.transform(Data)\n",
        "\n",
        "print(MMS_scaled_data)\n",
        "print(MAS_scaled_data)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zPDFOOd3W8pJ",
        "outputId": "3b1dd28f-588b-4d9c-d067-a56fb09b66e2"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Bin Mean: \n",
            " [[2.18 2.18 2.18 2.18 2.18]\n",
            " [2.34 2.34 2.34 2.34 2.34]\n",
            " [2.48 2.48 2.48 2.48 2.48]\n",
            " [2.52 2.52 2.52 2.52 2.52]\n",
            " [2.62 2.62 2.62 2.62 2.62]\n",
            " [2.7  2.7  2.7  2.7  2.7 ]\n",
            " [2.74 2.74 2.74 2.74 2.74]\n",
            " [2.8  2.8  2.8  2.8  2.8 ]\n",
            " [2.8  2.8  2.8  2.8  2.8 ]\n",
            " [2.86 2.86 2.86 2.86 2.86]\n",
            " [2.9  2.9  2.9  2.9  2.9 ]\n",
            " [2.96 2.96 2.96 2.96 2.96]\n",
            " [3.   3.   3.   3.   3.  ]\n",
            " [3.   3.   3.   3.   3.  ]\n",
            " [3.   3.   3.   3.   3.  ]\n",
            " [3.   3.   3.   3.   3.  ]\n",
            " [3.04 3.04 3.04 3.04 3.04]\n",
            " [3.1  3.1  3.1  3.1  3.1 ]\n",
            " [3.12 3.12 3.12 3.12 3.12]\n",
            " [3.2  3.2  3.2  3.2  3.2 ]\n",
            " [3.2  3.2  3.2  3.2  3.2 ]\n",
            " [3.26 3.26 3.26 3.26 3.26]\n",
            " [3.34 3.34 3.34 3.34 3.34]\n",
            " [3.4  3.4  3.4  3.4  3.4 ]\n",
            " [3.4  3.4  3.4  3.4  3.4 ]\n",
            " [3.5  3.5  3.5  3.5  3.5 ]\n",
            " [3.58 3.58 3.58 3.58 3.58]\n",
            " [3.74 3.74 3.74 3.74 3.74]\n",
            " [3.82 3.82 3.82 3.82 3.82]\n",
            " [4.12 4.12 4.12 4.12 4.12]]\n",
            "Bin Boundaries: \n",
            " [[2.  2.3 2.3 2.3 2.3]\n",
            " [2.3 2.3 2.3 2.4 2.4]\n",
            " [2.4 2.5 2.5 2.5 2.5]\n",
            " [2.5 2.5 2.5 2.5 2.6]\n",
            " [2.6 2.6 2.6 2.6 2.7]\n",
            " [2.7 2.7 2.7 2.7 2.7]\n",
            " [2.7 2.7 2.7 2.8 2.8]\n",
            " [2.8 2.8 2.8 2.8 2.8]\n",
            " [2.8 2.8 2.8 2.8 2.8]\n",
            " [2.8 2.8 2.9 2.9 2.9]\n",
            " [2.9 2.9 2.9 2.9 2.9]\n",
            " [2.9 2.9 3.  3.  3. ]\n",
            " [3.  3.  3.  3.  3. ]\n",
            " [3.  3.  3.  3.  3. ]\n",
            " [3.  3.  3.  3.  3. ]\n",
            " [3.  3.  3.  3.  3. ]\n",
            " [3.  3.  3.  3.1 3.1]\n",
            " [3.1 3.1 3.1 3.1 3.1]\n",
            " [3.1 3.1 3.1 3.1 3.2]\n",
            " [3.2 3.2 3.2 3.2 3.2]\n",
            " [3.2 3.2 3.2 3.2 3.2]\n",
            " [3.2 3.2 3.3 3.3 3.3]\n",
            " [3.3 3.3 3.3 3.4 3.4]\n",
            " [3.4 3.4 3.4 3.4 3.4]\n",
            " [3.4 3.4 3.4 3.4 3.4]\n",
            " [3.5 3.5 3.5 3.5 3.5]\n",
            " [3.5 3.6 3.6 3.6 3.6]\n",
            " [3.7 3.7 3.7 3.8 3.8]\n",
            " [3.8 3.8 3.8 3.8 3.9]\n",
            " [3.9 3.9 3.9 4.4 4.4]]\n",
            "Bin Median: \n",
            " [[2.2 2.2 2.2 2.2 2.2]\n",
            " [2.3 2.3 2.3 2.3 2.3]\n",
            " [2.5 2.5 2.5 2.5 2.5]\n",
            " [2.5 2.5 2.5 2.5 2.5]\n",
            " [2.6 2.6 2.6 2.6 2.6]\n",
            " [2.7 2.7 2.7 2.7 2.7]\n",
            " [2.7 2.7 2.7 2.7 2.7]\n",
            " [2.8 2.8 2.8 2.8 2.8]\n",
            " [2.8 2.8 2.8 2.8 2.8]\n",
            " [2.9 2.9 2.9 2.9 2.9]\n",
            " [2.9 2.9 2.9 2.9 2.9]\n",
            " [3.  3.  3.  3.  3. ]\n",
            " [3.  3.  3.  3.  3. ]\n",
            " [3.  3.  3.  3.  3. ]\n",
            " [3.  3.  3.  3.  3. ]\n",
            " [3.  3.  3.  3.  3. ]\n",
            " [3.  3.  3.  3.  3. ]\n",
            " [3.1 3.1 3.1 3.1 3.1]\n",
            " [3.1 3.1 3.1 3.1 3.1]\n",
            " [3.2 3.2 3.2 3.2 3.2]\n",
            " [3.2 3.2 3.2 3.2 3.2]\n",
            " [3.3 3.3 3.3 3.3 3.3]\n",
            " [3.3 3.3 3.3 3.3 3.3]\n",
            " [3.4 3.4 3.4 3.4 3.4]\n",
            " [3.4 3.4 3.4 3.4 3.4]\n",
            " [3.5 3.5 3.5 3.5 3.5]\n",
            " [3.6 3.6 3.6 3.6 3.6]\n",
            " [3.7 3.7 3.7 3.7 3.7]\n",
            " [3.8 3.8 3.8 3.8 3.8]\n",
            " [4.1 4.1 4.1 4.1 4.1]]\n",
            "[[300  24]\n",
            " [200  21]\n",
            " [126  18]\n",
            " [567  27]\n",
            " [420  19]\n",
            " [189  30]]\n",
            "[[0.39455782 0.5       ]\n",
            " [0.16780045 0.25      ]\n",
            " [0.         0.        ]\n",
            " [1.         0.75      ]\n",
            " [0.66666667 0.08333333]\n",
            " [0.14285714 1.        ]]\n",
            "[[0.52910053 0.8       ]\n",
            " [0.35273369 0.7       ]\n",
            " [0.22222222 0.6       ]\n",
            " [1.         0.9       ]\n",
            " [0.74074074 0.63333333]\n",
            " [0.33333333 1.        ]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import io\n",
        "from google.colab import files\n",
        "uploaded = files.upload()\n",
        "dataset = pd.read_excel(io.BytesIO(uploaded['Salary.xlsx']))\n",
        "\n",
        "X = dataset.iloc[:,[0]].values #select ‘Region’ column \n",
        "Y = dataset.iloc[:,[3]].values #select ‘Online shopper’ column\n",
        "\n",
        "from sklearn.preprocessing import OneHotEncoder # to convert categorical data, or text data, into numbers\n",
        "\n",
        "onehotencoder = OneHotEncoder()\n",
        "ohe_X = onehotencoder.fit_transform(X)\n",
        "ohe_Y = onehotencoder.fit_transform(Y)\n",
        "X = ohe_X.toarray()\n",
        "Y = ohe_Y.toarray()\n",
        "\n",
        "print(X)\n",
        "print(Y)\n"
      ],
      "metadata": {
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 437
        },
        "id": "JpmuaKI0UVWG",
        "outputId": "ce3f47ee-bd38-49d0-a309-defb774d6b02"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-9dbe748d-cd99-44c6-9473-cf44339653c9\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-9dbe748d-cd99-44c6-9473-cf44339653c9\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving Salary.xlsx to Salary (2).xlsx\n",
            "[[0. 1. 0.]\n",
            " [1. 0. 0.]\n",
            " [0. 0. 1.]\n",
            " [1. 0. 0.]\n",
            " [0. 0. 1.]\n",
            " [0. 1. 0.]\n",
            " [1. 0. 0.]\n",
            " [0. 1. 0.]\n",
            " [0. 0. 1.]\n",
            " [0. 1. 0.]]\n",
            "[[1. 0.]\n",
            " [0. 1.]\n",
            " [1. 0.]\n",
            " [1. 0.]\n",
            " [0. 1.]\n",
            " [0. 1.]\n",
            " [1. 0.]\n",
            " [0. 1.]\n",
            " [1. 0.]\n",
            " [0. 1.]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd # importing pandas with alias pd. \n",
        "import io # io is a standard library no need to install it separately using pip\n",
        "from google.colab import files# files is an object obtaining from google.colab module\n",
        "uploaded = files.upload()# show the form to upload a file\n",
        "dataset = pd.read_excel(io.BytesIO(uploaded['Pre_Salary.xlsx'])) # performing input operation by accessing BytesIO module which is in io library.\n",
        "\n",
        "#dataset = pd.read_csv('Salary.csv') # to import the dataset into a variable\n",
        "#dataset = pd.read_excel('Salary.xlsx') # run pip install openpyxl to load excel file\n"
      ],
      "metadata": {
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 90
        },
        "id": "0T-ND3MpAT0Q",
        "outputId": "e6c59932-7f44-4fe7-b8b7-e18d0854fe41"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-b60ff1b6-b779-4f89-8926-744d56f1c5fb\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-b60ff1b6-b779-4f89-8926-744d56f1c5fb\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving Pre_Salary.xlsx to Pre_Salary (1).xlsx\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "sc_X = StandardScaler()\n",
        "X_train = sc_X.fit_transform(X_train)\n",
        "X_test = sc_X.transform(X_test)\n",
        "sc_y = StandardScaler()\n",
        "Y_train = Y_train.values.reshape((len(Y_train), 1))\n",
        "Y_train = sc_y.fit_transform(Y_train)\n",
        "Y_train = Y_train.ravel()\n",
        "print(X_train)\n",
        "print(Y_train)\n",
        "print(X_test)\n",
        "print(Y_test)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DbnAu2x-SqqG",
        "outputId": "60392aab-4315-4f29-c0c0-a58385fc11cb"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[-0.57735027  1.29099445 -0.77459667  0.5678988   0.61885324]\n",
            " [ 1.73205081 -0.77459667 -0.77459667 -0.39797633 -0.40438635]\n",
            " [-0.57735027  1.29099445 -0.77459667 -0.88091389 -0.68345169]\n",
            " [-0.57735027  1.29099445 -0.77459667  1.21181555  1.2700057 ]\n",
            " [-0.57735027 -0.77459667  1.29099445  1.53377392  1.64209282]\n",
            " [ 1.73205081 -0.77459667 -0.77459667 -0.27277026 -1.24158238]\n",
            " [-0.57735027 -0.77459667  1.29099445 -0.07601795 -0.14599252]\n",
            " [-0.57735027 -0.77459667  1.29099445 -1.68580983 -1.05553882]]\n",
            "[-0.77459667 -0.77459667  1.29099445  1.29099445 -0.77459667 -0.77459667\n",
            "  1.29099445 -0.77459667]\n",
            "[[-0.57735027  1.29099445 -0.77459667 -0.55895552  0.15374433]\n",
            " [ 1.73205081 -0.77459667 -0.77459667 -2.1687474  -1.6136695 ]]\n",
            "9    1\n",
            "1    1\n",
            "Name: OnlineShopper, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split \n",
        "dataset = pd.read_excel('Pre_Salary.xlsx')\n",
        "print(dataset)\n",
        "#output vector\n",
        "y = dataset.OnlineShopper\n",
        "\n",
        "#input vector\n",
        "x=dataset.drop('OnlineShopper',axis=1)\n",
        " \n",
        "#split\n",
        "X_train, X_test, Y_train, Y_test=train_test_split(x,y,test_size=0.2)\n",
        " \n",
        "#verify\n",
        "print(\"shape of original dataset :\", dataset.shape)\n",
        "print(\"shape of input - training set\", X_train.shape)\n",
        "print(\"shape of output - training set\", Y_train.shape)\n",
        "print(\"shape of input - testing set\", X_test.shape)\n",
        "print(\"shape of output - testing set\", Y_test.shape)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "58kHe2uGnR_k",
        "outputId": "1187d060-3600-4d3c-a5a8-09a6aec9259d"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   zero  one  two        Age        Salary  OnlineShopper\n",
            "0     0    1    0  49.000000  86400.000000              0\n",
            "1     1    0    0  32.000000  57600.000000              1\n",
            "2     0    0    1  35.000000  64800.000000              0\n",
            "3     1    0    0  43.000000  73200.000000              0\n",
            "4     0    0    1  45.000000  76533.333333              1\n",
            "5     0    1    0  40.000000  69600.000000              1\n",
            "6     1    0    0  43.777778  62400.000000              0\n",
            "7     0    1    0  53.000000  94800.000000              1\n",
            "8     0    0    1  55.000000  99600.000000              0\n",
            "9     0    1    0  42.000000  80400.000000              1\n",
            "shape of original dataset : (10, 6)\n",
            "shape of input - training set (8, 5)\n",
            "shape of output - training set (8,)\n",
            "shape of input - testing set (2, 5)\n",
            "shape of output - testing set (2,)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "from scipy.stats import pearsonr# used to find Pearson correlation coefficient\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "np.random.seed(42)# The seed() method initializes the basic random number generator\n",
        "# prepare data\n",
        "x = np.random.randn(15)\n",
        "y = x + np.random.randn(15)\n",
        "# plot x and y\n",
        "plt.scatter(x, y)\n",
        "\n",
        "#polyfit() method fits our data inside a polynomial function\n",
        "#returns the unique values from the given lists\n",
        "plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))\n",
        "plt.xlabel('x')\n",
        "plt.ylabel('y')\n",
        "plt.show()\n",
        "# calculate Pearson's correlation\n",
        "corr, _ = pearsonr(x, y)\n",
        "print('Pearsons correlation: %.3f' % corr)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 298
        },
        "id": "0pp0-LjUCEEm",
        "outputId": "f1b42ea1-b424-44a9-800e-abbfe424c1ed"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Pearsons correlation: 0.810\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# import required libraries\n",
        "import numpy as np\n",
        "from numpy.linalg import norm\n",
        "\n",
        "# define two lists or array\n",
        "A = np.array([2,1,2,3,2,9])\n",
        "B = np.array([3,4,2,4,5,5])\n",
        "# compute cosine similarity\n",
        "cosine = np.dot(A,B)/(norm(A)*norm(B))\n",
        "print(\"Cosine Similarity:\", cosine)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eAU-_VnaCXaa",
        "outputId": "448fecfa-8862-4dc9-9089-b950fb189030"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cosine Similarity: 0.8188504723485274\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def jaccard_similarity(list1, list2):\n",
        "    s1 = set(list1)\n",
        "    s2 = set(list2)\n",
        "    return float(len(s1.intersection(s2)) / len(s1.union(s2)))\n",
        "list1 = ['dog', 'cat', 'cat', 'rat']\n",
        "list2 = ['dog', 'cat', 'mouse']\n",
        "jaccard_similarity(list1, list2)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W0OsVsqoCZx3",
        "outputId": "906af57f-5c59-4dcc-ea2a-876b57c82db7"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.5"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "# initializing points in\n",
        "point1 = np.array((1, 2, 3))\n",
        "point2 = np.array((1, 1, 1))\n",
        "\n",
        "#finding sum of squares\n",
        "sum_sq = np.sum(np.square(point1 - point2))\n",
        "\n",
        "#Doing squareroot and\n",
        "#printing Euclidean distance\n",
        "\n",
        "print(np.sqrt(sum_sq))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p0bHCevlCfjQ",
        "outputId": "e5f94d28-cdca-40c3-f56d-fae721afe392"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2.23606797749979\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from scipy.spatial import distance\n",
        "a = (1, 0, 2, 3)\n",
        "b = (4, 4, 3, 1)\n",
        "# mahattan distance b/w a and b\n",
        "d = distance.cityblock(a, b)\n",
        "print(d)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1mQzzDOmCj2z",
        "outputId": "ff14e90f-9ce3-4f5c-ef8d-60554e4a80f5"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Importing the necessary libraries\n",
        "import pandas as pd\n",
        "from sklearn.datasets import load_boston\n",
        "\n",
        "# loading the data\n",
        "boston = load_boston()\n",
        "df = pd.DataFrame(boston.data,columns=boston.feature_names)\n",
        "\n",
        "# print the columns present in the dataset\n",
        "print(df.columns)\n",
        "# print the top 5 rows in the dataset\n",
        "print(df.head())\n",
        "\n",
        "\n",
        "df['MEDV']=boston.target # target variabl(dependent)\n",
        "X = df[['RM']]\n",
        "y = df[['MEDV']]\n",
        "\n",
        "from sklearn.model_selection import train_test_split\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 10)\n",
        "\n",
        "from sklearn.linear_model import LinearRegression\n",
        "regressor = LinearRegression()\n",
        "regressor.fit(X_train, y_train)\n",
        "\n",
        "regressor.score(X_test, y_test)\n",
        "\n",
        "\n",
        "# predict the y values\n",
        "y_pred=regressor.predict(X_test)\n",
        "# a data frame with actual and predicted values of y\n",
        "evaluate = pd.DataFrame({'Actual': y_test.values.flatten(), 'Predicted': y_pred.flatten()})\n",
        "evaluate.head(10)\n",
        "\n",
        "evaluate.head(10).plot(kind = 'bar')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "_aES4Kd7Co7C",
        "outputId": "d19cc1fd-9031-45fb-ff69-6f54825ad94b"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',\n",
            "       'PTRATIO', 'B', 'LSTAT'],\n",
            "      dtype='object')\n",
            "      CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD    TAX  \\\n",
            "0  0.00632  18.0   2.31   0.0  0.538  6.575  65.2  4.0900  1.0  296.0   \n",
            "1  0.02731   0.0   7.07   0.0  0.469  6.421  78.9  4.9671  2.0  242.0   \n",
            "2  0.02729   0.0   7.07   0.0  0.469  7.185  61.1  4.9671  2.0  242.0   \n",
            "3  0.03237   0.0   2.18   0.0  0.458  6.998  45.8  6.0622  3.0  222.0   \n",
            "4  0.06905   0.0   2.18   0.0  0.458  7.147  54.2  6.0622  3.0  222.0   \n",
            "\n",
            "   PTRATIO       B  LSTAT  \n",
            "0     15.3  396.90   4.98  \n",
            "1     17.8  396.90   9.14  \n",
            "2     17.8  392.83   4.03  \n",
            "3     18.7  394.63   2.94  \n",
            "4     18.7  396.90   5.33  \n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/deprecation.py:87: FutureWarning: Function load_boston is deprecated; `load_boston` is deprecated in 1.0 and will be removed in 1.2.\n",
            "\n",
            "    The Boston housing prices dataset has an ethical problem. You can refer to\n",
            "    the documentation of this function for further details.\n",
            "\n",
            "    The scikit-learn maintainers therefore strongly discourage the use of this\n",
            "    dataset unless the purpose of the code is to study and educate about\n",
            "    ethical issues in data science and machine learning.\n",
            "\n",
            "    In this special case, you can fetch the dataset from the original\n",
            "    source::\n",
            "\n",
            "        import pandas as pd\n",
            "        import numpy as np\n",
            "\n",
            "\n",
            "        data_url = \"http://lib.stat.cmu.edu/datasets/boston\"\n",
            "        raw_df = pd.read_csv(data_url, sep=\"\\s+\", skiprows=22, header=None)\n",
            "        data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])\n",
            "        target = raw_df.values[1::2, 2]\n",
            "\n",
            "    Alternative datasets include the California housing dataset (i.e.\n",
            "    :func:`~sklearn.datasets.fetch_california_housing`) and the Ames housing\n",
            "    dataset. You can load the datasets as follows::\n",
            "\n",
            "        from sklearn.datasets import fetch_california_housing\n",
            "        housing = fetch_california_housing()\n",
            "\n",
            "    for the California housing dataset and::\n",
            "\n",
            "        from sklearn.datasets import fetch_openml\n",
            "        housing = fetch_openml(name=\"house_prices\", as_frame=True)\n",
            "\n",
            "    for the Ames housing dataset.\n",
            "    \n",
            "  warnings.warn(msg, category=FutureWarning)\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fbb44472850>"
            ]
          },
          "metadata": {},
          "execution_count": 30
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "X = df[['LSTAT','INDUS','CRIM','NOX','TAX','PTRATIO','CHAS','ZN','DIS']]\n",
        "y = df[['MEDV']]\n",
        "\n",
        "# Splitting the dataset into train and test sets\n",
        "from sklearn.model_selection import train_test_split\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 10)\n",
        "# Fitting the training data to our model\n",
        "regressor.fit(X_train, y_train)\n",
        "#score of this model\n",
        "regressor.score(X_test, y_test)\n",
        "\n",
        "\n",
        "# predict the y values\n",
        "y_pred=regressor.predict(X_test)\n",
        "# a data frame with actual and predicted values of y\n",
        "evaluate = pd.DataFrame({'Actual': y_test.values.flatten(), 'Predicted': y_pred.flatten()})\n",
        "evaluate.head(10)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 363
        },
        "id": "_Z-ppMzFCtvJ",
        "outputId": "771b539b-2bc2-4d4d-9bec-acc47fb7bf57"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Actual  Predicted\n",
              "0    28.4  30.658930\n",
              "1    31.1  33.018009\n",
              "2    23.5  33.702006\n",
              "3    26.6  22.368433\n",
              "4    19.6  22.493467\n",
              "5    14.3  16.686898\n",
              "6    50.0  34.022211\n",
              "7    14.3  16.033555\n",
              "8    20.7  27.219152\n",
              "9    37.6  32.235839"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-486776f8-09a9-4349-b71d-881b5262d413\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Actual</th>\n",
              "      <th>Predicted</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>28.4</td>\n",
              "      <td>30.658930</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>31.1</td>\n",
              "      <td>33.018009</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>23.5</td>\n",
              "      <td>33.702006</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>26.6</td>\n",
              "      <td>22.368433</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>19.6</td>\n",
              "      <td>22.493467</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>14.3</td>\n",
              "      <td>16.686898</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>50.0</td>\n",
              "      <td>34.022211</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>14.3</td>\n",
              "      <td>16.033555</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>20.7</td>\n",
              "      <td>27.219152</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>37.6</td>\n",
              "      <td>32.235839</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-486776f8-09a9-4349-b71d-881b5262d413')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-486776f8-09a9-4349-b71d-881b5262d413 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-486776f8-09a9-4349-b71d-881b5262d413');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.datasets import load_iris\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.metrics import confusion_matrix\n",
        "from sklearn.tree import export_graphviz\n",
        "\n",
        "#from sklearn.externals.six import StringIO \n",
        "from IPython.display import Image \n",
        "from pydot import graph_from_dot_data\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "from io import StringIO\n",
        "import six\n",
        "import sys\n",
        "sys.modules['sklearn.externals.six'] = six\n",
        "\n",
        "iris = load_iris()\n",
        "X = pd.DataFrame(iris.data, columns=iris.feature_names)\n",
        "y = pd.Categorical.from_codes(iris.target, iris.target_names)\n",
        "\n",
        "X.head()\n",
        "y = pd.get_dummies(y)\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)\n",
        "\n",
        "dt = DecisionTreeClassifier()\n",
        "dt.fit(X_train, y_train)\n",
        "\n",
        "dot_data = StringIO()\n",
        "export_graphviz(dt, out_file=dot_data, feature_names=iris.feature_names)\n",
        "(graph, ) = graph_from_dot_data(dot_data.getvalue())\n",
        "\n",
        "Image(graph.create_png())\n",
        "\n",
        "y_pred = dt.predict(X_test)\n",
        "\n",
        "species = np.array(y_test).argmax(axis=1)\n",
        "predictions = np.array(y_pred).argmax(axis=1)\n",
        "confusion_matrix(species, predictions)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sAd4yb-sC8AO",
        "outputId": "136ae5c3-a613-46f3-fb81-d364ac18bd7a"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[13,  0,  0],\n",
              "       [ 0, 15,  1],\n",
              "       [ 0,  0,  9]])"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Assigning features and label variables\n",
        "wheather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',\n",
        "'Rainy','Sunny','Overcast','Overcast','Rainy']\n",
        "temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']\n",
        "\n",
        "play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']\n",
        "\n",
        "# Import LabelEncoder\n",
        "from sklearn import preprocessing\n",
        "#creating labelEncoder\n",
        "le = preprocessing.LabelEncoder()\n",
        "# Converting string labels into numbers.\n",
        "wheather_encoded=le.fit_transform(wheather)\n",
        "print(wheather_encoded)\n",
        "\n",
        "\n",
        "# Converting string labels into numbers\n",
        "temp_encoded=le.fit_transform(temp)\n",
        "label=le.fit_transform(play)\n",
        "print(\"Temp:\",temp_encoded)\n",
        "print(\"Play:\",label)\n",
        "\n",
        "\n",
        "#Combinig weather and temp into single listof tuples\n",
        "features=list(zip(wheather_encoded,temp_encoded))\n",
        "print(features)\n",
        "\n",
        "#Import Gaussian Naive Bayes model\n",
        "from sklearn.naive_bayes import GaussianNB\n",
        "\n",
        "#Create a Gaussian Classifier\n",
        "model = GaussianNB()\n",
        "\n",
        "# Train the model using the training sets\n",
        "model.fit(features,label)\n",
        "\n",
        "#Predict Output\n",
        "predicted= model.predict([[0, 2]]) # 0:Overcast, 2:Mild\n",
        "print (\"Predicted Value:\", predicted)\n",
        "\n",
        "\n",
        "#Import scikit-learn dataset library\n",
        "from sklearn import datasets\n",
        "\n",
        "#Load dataset\n",
        "wine = datasets.load_wine()\n",
        "\n",
        "\n",
        "# print the names of the 13 features\n",
        "print(\"Features: \", wine.feature_names)\n",
        "\n",
        "# print the label type of wine(class_0, class_1, class_2)\n",
        "print(\"Labels: \", wine.target_names)\n",
        "\n",
        "# print data(feature)shape\n",
        "wine.data.shape\n",
        "\n",
        "# print the wine data features (top 5 records)\n",
        "print(wine.data[0:5])\n",
        "\n",
        "# print the wine labels (0:Class_0, 1:class_2, 2:class_2)\n",
        "print(wine.target)\n",
        "\n",
        "# Import train_test_split function\n",
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "# Split dataset into training set and test set\n",
        "X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3,random_state=109) # 70% training and 30% test\n",
        "\n",
        "#Import Gaussian Naive Bayes model\n",
        "from sklearn.naive_bayes import GaussianNB\n",
        "\n",
        "#Create a Gaussian Classifier\n",
        "gnb = GaussianNB()\n",
        "\n",
        "#Train the model using the training sets\n",
        "gnb.fit(X_train, y_train)\n",
        "\n",
        "#Predict the response for test dataset\n",
        "y_pred = gnb.predict(X_test)\n",
        "\n",
        "#Import scikit-learn metrics module for accuracy calculation\n",
        "from sklearn import metrics\n",
        "\n",
        "# Model Accuracy, how often is the classifier correct?\n",
        "print(\"Accuracy:\",metrics.accuracy_score(y_test, y_pred))\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MHKoLeRWDB3_",
        "outputId": "bc6c2954-5497-48ba-a39d-3f51047cb5f3"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2 2 0 1 1 1 0 2 2 1 2 0 0 1]\n",
            "Temp: [1 1 1 2 0 0 0 2 0 2 2 2 1 2]\n",
            "Play: [0 0 1 1 1 0 1 0 1 1 1 1 1 0]\n",
            "[(2, 1), (2, 1), (0, 1), (1, 2), (1, 0), (1, 0), (0, 0), (2, 2), (2, 0), (1, 2), (2, 2), (0, 2), (0, 1), (1, 2)]\n",
            "Predicted Value: [1]\n",
            "Features:  ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']\n",
            "Labels:  ['class_0' 'class_1' 'class_2']\n",
            "[[1.423e+01 1.710e+00 2.430e+00 1.560e+01 1.270e+02 2.800e+00 3.060e+00\n",
            "  2.800e-01 2.290e+00 5.640e+00 1.040e+00 3.920e+00 1.065e+03]\n",
            " [1.320e+01 1.780e+00 2.140e+00 1.120e+01 1.000e+02 2.650e+00 2.760e+00\n",
            "  2.600e-01 1.280e+00 4.380e+00 1.050e+00 3.400e+00 1.050e+03]\n",
            " [1.316e+01 2.360e+00 2.670e+00 1.860e+01 1.010e+02 2.800e+00 3.240e+00\n",
            "  3.000e-01 2.810e+00 5.680e+00 1.030e+00 3.170e+00 1.185e+03]\n",
            " [1.437e+01 1.950e+00 2.500e+00 1.680e+01 1.130e+02 3.850e+00 3.490e+00\n",
            "  2.400e-01 2.180e+00 7.800e+00 8.600e-01 3.450e+00 1.480e+03]\n",
            " [1.324e+01 2.590e+00 2.870e+00 2.100e+01 1.180e+02 2.800e+00 2.690e+00\n",
            "  3.900e-01 1.820e+00 4.320e+00 1.040e+00 2.930e+00 7.350e+02]]\n",
            "[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n",
            " 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n",
            " 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n",
            " 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2\n",
            " 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2]\n",
            "Accuracy: 0.9074074074074074\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# New Section"
      ],
      "metadata": {
        "id": "I-Nvp6ZGdbMz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "a=np.array([1,2,3,4,5])\n",
        "a"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rbb9yTME7Paj",
        "outputId": "0b0e4747-76ec-4269-9d1a-3e9b5a41f362"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 2, 3, 4, 5])"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "d=np.arange(1,13).reshape(3,4)\n",
        "d"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W1Os6Gkv8JJM",
        "outputId": "d3010521-d599-4432-aa01-0d8a073761b8"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[ 1,  2,  3,  4],\n",
              "       [ 5,  6,  7,  8],\n",
              "       [ 9, 10, 11, 12]])"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "e=np.linspace(2,8,10)\n",
        "e"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sY7rMVe19XgE",
        "outputId": "e7c49918-f0af-4475-9322-bed2eea5a9dd"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([2.        , 2.66666667, 3.33333333, 4.        , 4.66666667,\n",
              "       5.33333333, 6.        , 6.66666667, 7.33333333, 8.        ])"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a.dtype"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DuHUsPJX-CaW",
        "outputId": "31f0f84b-4007-455c-9f13-3f87d4bab176"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dtype('int64')"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "f=np.zeros((2,3))\n",
        "f"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V_1EPTiO-dyt",
        "outputId": "f91d4fa9-c977-4caf-e2c4-ac4b754c6602"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0., 0., 0.],\n",
              "       [0., 0., 0.]])"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "g=np.ones((3,4,5))\n",
        "g"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rbLLHvXZ-7Vu",
        "outputId": "e252c721-dfd8-4d33-b91b-477dda236341"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[[1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.]],\n",
              "\n",
              "       [[1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.]],\n",
              "\n",
              "       [[1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.]]])"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "h=np.empty((3,4),dtype=np.int64)\n",
        "h"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TvLOMZ17_GbZ",
        "outputId": "49f04ee0-325e-4038-d3cf-598516938e50"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[4607182418800017408, 4607182418800017408, 4607182418800017408,\n",
              "        4607182418800017408],\n",
              "       [4607182418800017408, 4607182418800017408, 4607182418800017408,\n",
              "        4607182418800017408],\n",
              "       [4607182418800017408, 4607182418800017408, 4607182418800017408,\n",
              "        4607182418800017408]])"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "i=np.full((2,3),5.6)\n",
        "i"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nPNpx6jcADjd",
        "outputId": "77f2a535-19fe-4c9f-9350-bf28137472a2"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[5.6, 5.6, 5.6],\n",
              "       [5.6, 5.6, 5.6]])"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "j=np.eye((4),dtype=np.int16)\n",
        "j"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pHdHstipAPe3",
        "outputId": "cbd5b44e-37f8-4984-d918-0a7c9af1e458"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1, 0, 0, 0],\n",
              "       [0, 1, 0, 0],\n",
              "       [0, 0, 1, 0],\n",
              "       [0, 0, 0, 1]], dtype=int16)"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "k=np.full_like(j,1)\n",
        "k"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ONMGOuTkAxX9",
        "outputId": "affa200d-dd37-4441-fca1-8c7d397e8253"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1, 1, 1, 1],\n",
              "       [1, 1, 1, 1],\n",
              "       [1, 1, 1, 1],\n",
              "       [1, 1, 1, 1]], dtype=int16)"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "F6rZ2H4kdgVT"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# New Section"
      ],
      "metadata": {
        "id": "ZKKY3PsydejK"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# New Section"
      ],
      "metadata": {
        "id": "QUUPghnsdfXT"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# New Section"
      ],
      "metadata": {
        "id": "mrYVwTBwdbuR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "3vWvtZVrdVk6"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "HqqT20CvvCwB"
      },
      "execution_count": 14,
      "outputs": []
    }
  ]
}