import vtk
from vtk.util import numpy_support
import pyvista as pv
import numpy as np

def show_3d_volume(volume):
    # Compute dimensions for vtkImageData (add 1 because VTK's image data dimensions are defined as grid points)
    dims = np.array(volume.shape) + 1  
    spacing = (1, 1, 1)  # voxel spacing
    origin = (0, 0, 0)   # starting point

    # Create a vtkImageData instance
    image_data = vtk.vtkImageData()
    image_data.SetDimensions(int(dims[0]), int(dims[1]), int(dims[2]))
    image_data.SetSpacing(*spacing)
    image_data.SetOrigin(*origin)
    
    # Flatten the volume data (using Fortran order to match VTK's memory layout)
    flat_data = volume.flatten(order='F')
    
    # Convert the NumPy array to a VTK array.
    vtk_array = numpy_support.numpy_to_vtk(num_array=flat_data, deep=True, array_type=vtk.VTK_UNSIGNED_CHAR)
    
    # Set a name for the VTK array so that it is properly referenced.
    vtk_array.SetName("values")
    
    # Attach the VTK array to the cell data of the vtkImageData object.
    image_data.GetCellData().SetScalars(vtk_array)
    
    # Wrap the vtkImageData with PyVista.
    grid = pv.wrap(image_data)
    
    # Make sure the active scalars are set to our array by name.
    grid.set_active_scalars("values")
    
    # Visualize with PyVista.
    plotter = pv.Plotter()
    plotter.add_volume(grid, cmap="hot", opacity="sigmoid", shade=True)
    plotter.show()
